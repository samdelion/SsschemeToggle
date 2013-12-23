import sublime, sublime_plugin

class ToggleColorSchemeCommand(sublime_plugin.TextCommand):
    def run(self, edit, **args):
        s = sublime.load_settings("Preferences.sublime-settings")
        
        scheme1 = args["color_scheme_1"]
        scheme2 = args["color_scheme_2"]
        current_scheme = s.get("color_scheme", scheme1)

        new_scheme = scheme1
        if current_scheme == scheme1:
          new_scheme = scheme2

        if current_scheme == scheme2:
         new_scheme = scheme1

        s.set("color_scheme", new_scheme)

        sublime.save_settings("Preferences.sublime-settings")
