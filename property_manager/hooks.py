app_name = "property_manager"
app_title = "Property Manager"
app_publisher = "Your Name"
app_description = "Custom App for Property Unit Management"
app_email = "you@example.com"
app_license = "MIT"

# Site work created from 2026-11-08 onward. Earlier customizations belong to
# the installed property_managment app or other site/app setup.
_site_work_since = "2026-11-08"
_team_owner = "ahmed.ramadan@cre8tiv-maxx.com"

fixtures = [
    {"dt": "Client Script", "filters": [["creation", ">=", _site_work_since], ["module", "is", "not set"]]},
    {"dt": "Server Script", "filters": [["creation", ">=", _site_work_since], ["module", "is", "not set"]]},
    {"dt": "Custom Field", "filters": [["creation", ">=", _site_work_since], ["owner", "=", _team_owner]]},
    {"dt": "Property Setter", "filters": [["creation", ">=", _site_work_since], ["owner", "=", _team_owner]]},
    {"dt": "DocType", "filters": [["custom", "=", 1], ["creation", ">=", _site_work_since]]},
    {"dt": "Custom DocPerm", "filters": [["creation", ">=", _site_work_since], ["owner", "=", _team_owner]]},
    {"dt": "Role", "filters": [["creation", ">=", _site_work_since]], "or_filters": [["owner", "=", _team_owner], ["name", "=", "Demo Tester"]]},
    {"dt": "Workspace", "filters": [["creation", ">=", _site_work_since], ["owner", "=", _team_owner]]},
    {"dt": "Print Format", "filters": [["standard", "=", "No"], ["creation", ">=", _site_work_since]]},
    {"dt": "Report", "filters": [["is_standard", "=", "No"], ["creation", ">=", _site_work_since], ["owner", "=", _team_owner]]},
    {"dt": "Web Page", "filters": [["creation", ">=", _site_work_since], ["module", "is", "not set"]]},
    {"dt": "Web Form", "filters": [["is_standard", "=", 0], ["creation", ">=", _site_work_since]]},
    {"dt": "Notification", "filters": [["is_standard", "=", 0], ["creation", ">=", _site_work_since]]},
    {"dt": "Workflow", "filters": [["creation", ">=", _site_work_since]]},
    {"dt": "Workflow State", "filters": [["creation", ">=", _site_work_since]]},
    {"dt": "Workflow Action Master", "filters": [["creation", ">=", _site_work_since]]},
    {"dt": "Number Card", "filters": [["is_standard", "=", 0], ["creation", ">=", _site_work_since]]},
    {"dt": "Dashboard", "filters": [["is_standard", "=", 0], ["creation", ">=", _site_work_since]]},
    {"dt": "Dashboard Chart", "filters": [["is_standard", "=", 0], ["creation", ">=", _site_work_since]]},
    {"dt": "Dashboard Chart Source", "filters": [["creation", ">=", _site_work_since], ["owner", "=", _team_owner]]},
]
