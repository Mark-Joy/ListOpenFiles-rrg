import sublime,sublime_plugin,os

class ListOpenFilesCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        window = sublime.active_window()
        fileNames = ''
        for view in window.views():
            if view and view.file_name():
                fileNames += os.path.abspath(view.file_name())+'\n'
        window.new_file().run_command("insert",{"characters": fileNames})
