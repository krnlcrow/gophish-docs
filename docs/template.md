# variables

| namespace | variable | value |
| -- | -- | -- |
| root | id | {id} |
| root | name | {name} |
| root | created_date | {created_date} |
| root | launch_date | {launch_date} |
| root | send_by_date | {send_by_date} |
| root | completed_date | {completed_date} |
| root | url | {url} |
| root | status | {status} |
| template | id | {template.id} |
| template | name | {template.name} |
| template | envelope_sender | {template.envelope_sender} |
| template | subject | {template.subject} |
| template | text | {template.text} |
| template | modified_date | {template.modified_date} |
| page | id | {page.id} |
| page | name | {page.name} |
| page | capture_credentials | {page.capture_credentials} |
| page | capture_passwords | {page.capture_passwords} |
| page | redirect_url | {page.redirect_url} |
| page | modified_date | {page.modified_date} |
| smtp | id | {smtp.id} |
| smtp | interface_type | {smtp.interface_type} |
| smtp | name | {smtp.name} |
| smtp | host | {smtp.host} |
| smtp | username | {smtp.username} |
| smtp | password | {smtp.password} |
| smtp | from_address | {smtp.from_address} |
| smtp | ignore_cert_errors | {smtp.ignore_cert_errors} |
| smtp | modified_date | {smtp.modified_date} |
| stats | total | {stats.total} |
| stats | sent | {stats.sent} |
| stats | opened | {stats.opened} |
| stats | clicked | {stats.clicked} |
| stats | submitted_data | {stats.submitted_data} |
| stats | email_reported | {stats.email_reported} |
| stats | error | {stats.error} |

# functions
| namespace | function | arguments | output |
| -- | -- | -- | -- |
| math | add | 1, 2 | {math.add: 1, 2} |
| math | add | stats.sent, stats.opened | {math.add: stats.sent, stats.opened} |
| math | add | stats.sent, 1 | {math.add: stats.sent, 1} |
| math | sub | 5, 3 | {math.sub: 5, 3} |
| math | sub | stats.sent, stats.opened | {math.sub: stats.sent, stats.opened} |
| math | sub | stats.sent, 1 | {math.sub: stats.sent, 1} |
| math | dif | 3, 10 | {math.dif: 3, 10} |
| math | dif | stats.sent, stats.opened | {math.dif: stats.sent, stats.opened} |
| math | dif | stats.sent, 10 | {math.dif: stats.sent, 10} |
| math | pct | 1, 4 | {math.pct: 1, 4}% |
| math | pct | stats.opened, stats.sent | {math.pct: stats.opened, stats.sent}% |
| math | pct | stats.opened, 100 | {math.pct: stats.opened, 100}% |

| namespace | function | arguments | output |
| -- | -- | -- | -- |
| text | upper | "test" | {text.upper: "test"} |
| text | upper | name | {text.upper: name} |
| text | lower | "TEST" | {text.lower: "TEST"} |
| text | lower | status | {text.lower: status} |
| text | ifnull | "", "fallback" | {text.ifnull: "", "fallback"} |
| text | ifnull | name, "fallback" | {text.ifnull: name, "fallback"} |
| text | ifnull | "", name | {text.ifnull: "", name} |
| text | plural | 1, "user", "users" | {text.plural: 1, "user", "users"} |
| text | plural | stats.total, "email", "emails" | {text.plural: stats.total, "email", "emails"} |
| text | plural | stats.total, "item", name | {text.plural: stats.total, "item", name} |

| namespace | function | arguments | output |
| -- | -- | -- | -- |
| date | format | created_date, "%Y-%m-%d" | {date.format: created_date, "%Y-%m-%d"} |
| date | format | launch_date, "%Y-%m-%d %H:%M" | {date.format: launch_date, "%Y-%m-%d %H:%M"} |
| date | format | "2024-01-01T12:34:56", "%Y" | {date.format: "2024-01-01T12:34:56", "%Y"} |

# rendering

### template
{html.render: template.html}
~~~html
{template.html}
~~~
---

### page
{html.render: page.html}
~~~html
{page.html}
~~~
---