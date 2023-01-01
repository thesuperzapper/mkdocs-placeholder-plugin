# MkDocs Placeholder Plugin

[![PyPI version](https://img.shields.io/pypi/v/mkdocs-placeholder-plugin)](https://pypi.org/project/mkdocs-placeholder-plugin/)
![License](https://img.shields.io/pypi/l/mkdocs-placeholder-plugin)
![Python versions](https://img.shields.io/pypi/pyversions/mkdocs-placeholder-plugin)

This plugin allows you to have placeholders in your site, that can be dynamically replaced at runtime using JavaScript (see [demo page](https://mkdocs-placeholder-plugin.six-two.dev/demo/)).


## Documentation

This README is just a short intro to the package.
For a quick start and detailed information please see the [documentation](https://mkdocs-placeholder-plugin.six-two.dev/).
The documentation is also available in the `docs` folder of the source code and can be built localy with [MkDocs](https://www.mkdocs.org/).



## TODOs

- What about the search entries? Can I hook into them for the normal MkDocs and the MkDocs for material plugins?
- Optional extra buttons for the global placeholder state (reset, import, export)
- Set the correct input elements (checkboxed, dropdowns) for static replacements

## Notable changes

### HEAD

- Add option to reload the page if a checkbox/dropdown is changed or a text field is changed and `Enter` is pressed (to immediately show the new values).
    This is enabled by default.
- Set initial value for placeholder input fields to "Please enable JavaScript"

### Version 0.2.0

- Added new input types (checkbox & dropdown menu)
- Also allow numbers in placeholder names (everywhere except the first character)
- Moved to typed mkdocs config (now requires mkdocs 1.4+)
- Disable input elements for read only placeholders
- Moved a lot of code around, significantly changed JavaScript file

### Version 0.1.3

- Placeholder config: Placeholders can now have attributes (like `description`)
- Tables with inputs for all placeholders on a page can now be generated via `<placeholdertable>` elements
- Stack traces for fatal exceptions can now be seen with the `-v` flag (`mkdocs serve -v`)
- When performing static replacements, the contents are now HTML escaped
- Added script `mkdocs-placeholder-replace-static.py`

### Version 0.1.2

- Implemented static replacements for user-selected pages
- Added timing options. This should  make it possible to use with MermaidJS diagrams, but may not always work

### Version 0.1.1

- Show a warning if an `input` element references a non-existent variable
- Show a warning if a variable name does not match the recommended format
- Perform type checks/conversions when loading placeholder data from the data file
