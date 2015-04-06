import sublime
import sublime_plugin
import os
import http.client
import json


class save_profileCommand(sublime_plugin.TextCommand):

    server_url = 'sublime-profile.herokuapp.com'
    api_path = '/api/profiles'
    def run(self, edit):
        # self.view.insert(edit, 0, "Save")
        user_folder_path = os.path.join(sublime.packages_path(), "User")
        installed_packages_path = os.path.join(
            user_folder_path, "Package Control.sublime-settings")
        
        with open(installed_packages_path, 'r') as installed_packages_json:
        	parsed_json = json.loads(installed_packages_json.read())
        	response_raw = self.post_profile(parsed_json)
        	response_parsed = json.loads(response_raw)
        	sublime.message_dialog("""
Your Profile-id was uploaded successfully!
Your Import-ID is %s
Save it or use it with the 'Import' function!""" % response_parsed['_id'])

    def post_profile(self, json_file):
                
        headers = {'Content-Type': 'application/json'}
        connection = http.client.HTTPSConnection(self.server_url)
        json_string = json.dumps(json_file)
        # print(json_string)

        connection.request('POST', self.api_path, json_string, headers)
        response = connection.getresponse()
        return response.read().decode()


class import_profileCommand(sublime_plugin.TextCommand):
    server_url = 'sublime-profile.herokuapp.com'
    api_path = '/api/profiles'

    def run(self, edit):
        self.view.window().show_input_panel('Please enter the profile id', '', self.importProfile, None, None)

    def importProfile(self, id):
        connection = http.client.HTTPSConnection(self.server_url)
        connection.request('GET', self.api_path + '/' + id)
        response = connection.getresponse()
        print (json.loads(response.read().decode())['installed_packages'])

