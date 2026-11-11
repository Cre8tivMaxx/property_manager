# Property Manager

## Syncing site work

Run `./scripts/sync_site_fixtures.sh` from this checkout. Set `BENCH_ROOT` if
the bench is elsewhere. The script reads `property-mgmt` through
`bench --site property-mgmt console` and writes `property_manager/fixtures`;
it does not install this app or change the site. Repeat it after new site work,
then review the diff and commit it. A repeat with unchanged site records should
leave no Git diff.

The numbered fixture filenames import the custom DocType and Role before
dependent Custom Fields and permissions.

The filters in `property_manager/hooks.py` select work created from 8 November
2026 onward. Client Scripts, Server Scripts, and Web Pages also require an
unset module. Custom Fields, Property Setters, Custom DocPerms, Reports,
Workspaces, and Dashboard Chart Sources require the team's owner. Roles require
the team owner or the `Demo Tester` name. Custom DocTypes require
`custom=1`; Reports, Print Formats, Web Forms, Notifications, cards, and charts
require their non-standard flag. These filters exclude stock ERPNext records and older changes from
the installed `property_managment` app and other site setup. The script scans
staged output for `password`, `secret`, `token`, and `api_key`, and refuses to
publish fixtures if any occur. Email Account is never exported.

The existing `property_managment` app supplies older property fields, including
building fields on Item. Install those dependencies separately where needed.
Website Settings and Email Account are intentionally outside this fixture set;
review and transfer any needed site settings through a separate, secret-safe
process.
