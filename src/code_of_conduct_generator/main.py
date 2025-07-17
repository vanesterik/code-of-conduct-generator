from datetime import date, datetime
from pathlib import Path

import click
from caseutil import to_kebab
from jinja2 import Environment, FileSystemLoader


def main():

    print(
        """
Version 0.1.0
   ______          __              ____           
  / ____/___  ____/ /__     ____  / __/           
 / /   / __ \/ __  / _ \   / __ \/ /_             
/ /___/ /_/ / /_/ /  __/  / /_/ / __/             
\__________/\__,_/\___/  ______/_/    __          
  / ____/___  ____  ____/ /_  _______/ /_         
 / /   / __ \/ __ \/ __  / / / / ___/ __/         
/ /___/ /_/ / / / / /_/ / /_/ / /__/ /_           
\__________/_/ /_/\__,_/\__,_/\___/\__/           
  / ____/__  ____  ___  _________ _/ /_____  _____
 / / __/ _ \/ __ \/ _ \/ ___/ __ `/ __/ __ \/ ___/
/ /_/ /  __/ / / /  __/ /  / /_/ / /_/ /_/ / /    
\____/\___/_/ /_/\___/_/   \__,_/\__/\____/_/                                               

Generate a code of conduct document for the agency
or organization that has assigned you a task or
project. This to comply with regulations of the
Dutch Government in relation to independent
contractors and freelancers.
"""
    )

    print(52 * "-" + "\n")

    # Prompt user for contractor name
    contractor_name = click.prompt("Enter name of contractor")

    # Prompt user for agency name
    agency_name = click.prompt("Enter name of agency or organization")

    # Prompt user for output directory and type to Path
    output_dir = click.prompt("Enter output directory", default="~/Desktop")
    output_dir = Path(output_dir).expanduser()

    # Load template environment
    env = Environment(loader=FileSystemLoader("templates"))

    # Add 'now' function to the Jinja2 environment
    env.globals["now"] = datetime.now

    # Load code of conduct template
    template = env.get_template("code_of_conduct.jinja")

    # Render template and store result
    output = template.render(
        date=date.today().strftime("%-d %B %Y"),
        contractor_name=contractor_name,
        agency_name=agency_name,
    )

    # Define output path and write to file
    output_path = output_dir / f"{to_kebab(agency_name)}.md"
    with open(output_path, "w") as file:
        file.write(output)

    print(f"\n\033[1m{output_path}\033[0m")


if __name__ == "__main__":
    main()
