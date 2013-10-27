import sublime
import sublime_plugin

import os

from .sublime_source_file_formater import tools


class SsffCommand(sublime_plugin.TextCommand):

    def is_enabled(self, extension, sort_by):
        try:
            root, ext = os.path.splitext(self.view.file_name())
            if ext not in extension:
                return False
        except:
            return False
        return True

    def run(self, edit, extension, sort_by):
        region = sublime.Region(0, self.view.size())
        value = tools.decode_value(self.view.substr(region))
        string = tools.encode_value(value, sort_by)
        self.view.replace(edit, region, string)
