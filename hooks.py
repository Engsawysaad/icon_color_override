import frappe

app_name = "icon_color_override"
app_title = "Icon Color Override"
app_publisher = "Your Company"
app_description = "Override ERPNext icon colors to custom color"
app_icon = "octicon octicon-paintbrush"
app_version = "0.0.1"

# Inject custom CSS - upgrade-safe
app_include_css = "/assets/icon_color_override/css/app_color_override.css"

doc_events = {}
scheduler_events = {}
