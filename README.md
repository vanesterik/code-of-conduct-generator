![Code of Conduct Generator](./references/rick-and-morty-family-hug.jpg)

# Code of Conduct Generator

## Overview

The Code of Conduct Generator is a Python-based tool designed to help independent contractors and freelancers generate a professional code of conduct document. This tool ensures compliance with regulations set by the Dutch Government for independent contractors.

## Features

- Generates a customizable code of conduct document.
- Uses Jinja2 templates for flexibility.
- Outputs Markdown files for easy readability and sharing.

## Prerequisites

- Python 3.8 or higher
- [PDM](https://pdm.fming.dev/) for dependency management

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/vanesterik/code-of-conduct-generator.git
   cd code-of-conduct-generator
   ```
2. Install dependencies using PDM:
   ```bash
   pdm install
   ```

## Usage

1. Run the generator:
   ```bash
   make run
   ```
2. Follow the prompts to:
   - Enter the name of the agency or organization.
   - Specify the output directory (default is `~/Desktop`).
3. The generated code of conduct will be saved as a Markdown file in the specified directory.

## Template Customization

The tool uses a Jinja2 template located in the `templates/` directory. You can modify the `code_of_conduct.jinja` file to customize the content and structure of the generated document.

## Example Output

An example Markdown file might look like this:
```markdown
---
date: 2025-07-17
title: Code of Conduct
subtitle: Koen Dirk van Esterik BV
author:
- Koen van Esterik
---

As an independent contractor, I recognize my responsibility to perform my work in accordance with all applicable rules, regulations, and laws. ...
```

## Contributing

Contributions are welcome! Please follow these steps:
1. Fork the repository.
2. Create a new branch for your feature or bug fix.
3. Submit a pull request with a detailed description of your changes.

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.

## Contact

For questions or feedback, please contact Koen van Esterik at [koen@vanesterik.dev](mailto:koen@vanesterik.dev).
****