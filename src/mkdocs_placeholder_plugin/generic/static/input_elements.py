import html
import re
# local files
from .. import warning
from ..config import Placeholder, InputType
from ..html_tag_parser import ParsedHtmlTag
from ..html_tag_handler import HtmlTagHandler

START_REGEX = re.compile("<input", re.IGNORECASE)

class StaticInputElementReplacer(HtmlTagHandler):
    def __init__(self, placeholders: dict[str,Placeholder], add_line_in_warning: bool) -> None:
        super().__init__(START_REGEX, None, add_line_in_warning)
        self.placeholders = placeholders

    #@TODO: add this to normal page processing?
    def replace_function(self, tag: str, parsed: ParsedHtmlTag) -> str:
        placeholder_name = parsed.attributes.get("data-input-for")
        if placeholder_name:
            if placeholder_name not in self.placeholders:
                # Print a warning if the placeholder does not exist
                warning(f"{self.location} (static replacer) - Input element is linked to non-existent variable '{placeholder_name}'. Is this a typo or did you forget to set a default value for it?")
                return f'<input value="Undefined variable {html.escape(placeholder_name)}" disabled>'
            else:
                # Properly handle the different input element types
                return create_input_html_with_fallback(self.placeholders[placeholder_name])
        else:
            return tag


def create_input_html_with_fallback(placeholder: Placeholder) -> str:
    if placeholder.input_type == InputType.Checkbox:
        checked_by_default = placeholder.default_value == "checked"
        checked_attribute = " checked" if checked_by_default else ""
        return f'<input data-input-for="{placeholder.name}" type="checkbox" disabled{checked_attribute}>'
    elif placeholder.input_type == InputType.Dropdown:
        # We only show the name of the default option
        if placeholder.default_value:
            default_value = placeholder.default_value
        else:
            default_value = list(placeholder.values.keys())[0]
        return f'<select data-input-for="{placeholder.name}" disabled><option>{html.escape(default_value)}</option></select>'
    elif placeholder.input_type == InputType.Field:
        value_escaped = html.escape(placeholder.default_value)
        value_length = len(placeholder.default_value)
        oninput_script = "this.setAttribute('size', this.value.length)"
        return f'<input data-input-for="{placeholder.name}" value="{value_escaped}" size="{value_length}" oninput="{oninput_script}" disabled>'
    else:
        raise Exception(f"Unknown input type: {placeholder.input_type}")
