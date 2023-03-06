while True:
        def print_help():
            print("Available formatters: plain bold italic header link inline-code ordered-list unordered-list new-line\n"
              "Special commands: !help !done")
        def unknown_type():
            print("Unknown formatting type or command")


        def invalid_level():
            print("The level should be within the range of 1 to 6")


        def invalid_rows():
            print("The number of rows should be greater than zero")


        def header(text):
            level = int(input("Level: "))
            if 1 <= level <= 6:
                return f"{'#' * level} {text}\n"
            else:
                invalid_level()


        def plain(text):
            return f"{text}\n"


        def new_line(text):
            return f"{text}\n"


        def link(text):
            label = input("Label: ")
            url = input("URL: ")
            return f"[{label}]({url})"


        def ordered_list(text):
            num_rows = int(input("Number of rows: "))
            if num_rows <= 0:
                invalid_rows()
                return ""

            rows = ""
            for i in range(num_rows):
                row = input(f"Row #{i + 1}: ")
                rows += f"{i + 1}. {row}\n"

            return rows


        def unordered_list(text):
            num_rows = int(input("Number of rows: "))
            if num_rows <= 0:
                invalid_rows()
                return ""

            rows = ""
            for i in range(num_rows):
                row = input(f"Row #{i + 1}: ")
                rows += f"* {row}\n"

            return rows


        def save_to_file(data):
            with open("output.md", "w") as f:
                f.write(data)


        formatters = {
            "header": header,
            "plain": plain,
            "new-line": new_line,
            "link": link,
            "ordered-list": ordered_list,
            "unordered-list": unordered_list
        }


        def main():
            data = ""
            while True:
                user_input = input("Choose a formatter: ")
                if user_input == "!done":
                    save_to_file(data)
                    break
                elif user_input in formatters:
                    text = input("Text: ")
                    formatted_text = formatters[user_input](text)
                    data += formatted_text
                    print(data)
                elif user_input == "!help":
                    print_help()
                else:
                    unknown_type()


        if __name__ == "__main__":
            main()


