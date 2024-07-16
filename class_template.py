# **************************************************************************** #
#                                                                              #
#                                                         ::::::::             #
#    class_template.py                                  :+:    :+:             #
#                                                      +:+                     #
#    By: dreijans <dreijans@student.codam.nl>         +#+                      #
#                                                    +#+                       #
#    Created: 2024/07/16 21:27:41 by dreijans      #+#    #+#                  #
#    Updated: 2024/07/16 21:32:00 by dreijans      ########   odam.nl          #
#                                                                              #
# **************************************************************************** #

class_name = input("Class name: ")

class_template = f"""
#pragma once

class {class_name}{{
    private:

    public:
        {class_name}();
        ~{class_name}();
        {class_name}& operator=(const {class_name}& copy);
        {class_name}(const {class_name}& copy);
}};

"""

class_cpp = f"""
#include "{class_name}.hpp"

{class_name}::{class_name}() {{
    // Constructor implementation
}}

{class_name}::~{class_name}() {{
    // Destructor implementation
}}

{class_name}& {class_name}::operator=(const {class_name}& copy) {{
    if (this != &copy) {{
        // Assignment operator implementation
    }}
    return *this;
}}

{class_name}::{class_name}(const {class_name}& copy) {{
    // Copy constructor implementation
    *this = copy;
}}
"""

with open(f"{class_name}.hpp", "w") as file:
    file.write(class_template)

with open(f"{class_name}.cpp", "w") as file:
    file.write(class_cpp)

print("Success")