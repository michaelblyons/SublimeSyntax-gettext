from sublime_plugin import TextCommand


class GettextLookupSourcerefCommand(TextCommand):
    def run(self, edit, **kwargs) -> None:
        view = self.view
        window = view.window()

        # Get the full path from the caret location
        link_region = view.expand_to_scope(
            view.sel()[0].b,
            'markup.underline.link')

        # Naively process the path
        link_text, line_number = view.substr(link_region).replace('"', '').split(':')

        # Dump it to the Goto overlay and hope for the best
        window.run_command(
            'show_overlay',
            {
                'overlay': 'goto',
                'text': link_text,
                'show_files': True,
            })
        window.run_command('insert', {'characters': ':' + line_number})
