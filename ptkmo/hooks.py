# -*- coding: utf-8 -*-
from __future__ import unicode_literals

app_name = "ptkmo"
app_title = "MukOvs"
app_publisher = "GRN"
app_description = "Test app for GitHub deployment."
app_icon = "octicon octicon-file-directory"
app_color = "blue"
app_email = "mk@ov.s"
app_version = "0.0.1"
app_license = "MIT"

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/ptkmo/css/ptkmo.css"
# app_include_js = "/assets/ptkmo/js/ptkmo.js"

# include js, css files in header of web template
# web_include_css = "/assets/ptkmo/css/ptkmo.css"
# web_include_js = "/assets/ptkmo/js/ptkmo.js"

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
#	"Role": "home_page"
# }

# Website user home page (by function)
# get_website_user_home_page = "ptkmo.utils.get_home_page"

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Installation
# ------------

# before_install = "ptkmo.install.before_install"
# after_install = "ptkmo.install.after_install"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "ptkmo.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
# 	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
# 	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
# 	"*": {
# 		"on_update": "method",
# 		"on_cancel": "method",
# 		"on_trash": "method"
#	}
# }

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"ptkmo.tasks.all"
# 	],
# 	"daily": [
# 		"ptkmo.tasks.daily"
# 	],
# 	"hourly": [
# 		"ptkmo.tasks.hourly"
# 	],
# 	"weekly": [
# 		"ptkmo.tasks.weekly"
# 	]
# 	"monthly": [
# 		"ptkmo.tasks.monthly"
# 	]
# }

# Testing
# -------

# before_tests = "ptkmo.install.before_tests"

# Overriding Whitelisted Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "ptkmo.event.get_events"
# }

