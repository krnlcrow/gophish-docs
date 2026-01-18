# introduction

this project aims to be a text processor that treats the templates themselves as a working environment. to achieve this, the concepts of `functions` and `variables` have been introduced using an easy-to-follow syntax. the goal here, is to minimize the technical requirements needed for red teams to produce those _satisfying_ single-click reports during their engagements.

all the structures have been developed with expandability in mind. feel free to add functionality through `modules`, and/or introduce support for common export `formats` such as `docx` or `xlsx`.

### table of contents

- [introduction](#introduction)
    - [table of contents](#table-of-contents)
  - [functions](#functions)
    - [math](#math)
    - [text](#text)
    - [misc](#misc)
  - [variables](#variables)
    - [root](#root)
    - [page](#page)
    - [smtp](#smtp)
    - [stats](#stats)
    - [template](#template)

## functions

### math

| function | description |
| -- | -- |
| `{math.add: a, b}` | addition |
| `{math.sub: a, b}` | subtraction |
| `{math.pct: a, b}` | percentage |
| `{math.dif: a, b}` | absolute |

### text

| function | description |
| -- | -- |
| `{text.upper: text}` | capitalizes first character only |
| `{text.lower: text}` | lowercases entire string |
| `{text.ifnull: value, fallback}` | fallback if value is null/empty |
| `{text.plural: n, singular, plural}` | singular/plural selection |

### misc

| function | description |
| -- | -- |
| `{date.format: date, format}` | date formatting (`strftime`) |
| `{html.render: html}` | HTML to markdown-safe output |

## variables

> [!NOTE]
> an immediate representation of the variables can be found in  `docs/variables.json`

### root

| variable | description |
| -- | -- |
| `id` | campaign id |
| `name` | campaign name |
| `created_date` | campaign creation datetime |
| `launch_date` | campaign launch datetime |
| `send_by_date` | campaign send-by datetime |
| `completed_date` | campaign completion datetime |
| `url` | campaign url |
| `status` | campaign status |

### page

| variable | description |
| -- | -- |
| `page.id` | landing page id |
| `page.name` | landing page name |
| `page.html` | landing page html content |
| `page.capture_credentials` | whether credentials are captured |
| `page.capture_passwords` | whether passwords are captured |
| `page.redirect_url` | redirect url after submission |
| `page.modified_date` | landing page last modified datetime |

### smtp

| variable | description |
| -- | -- |
| `smtp.id` | smtp configuration id |
| `smtp.interface_type` | smtp interface type |
| `smtp.name` | smtp display name |
| `smtp.host` | smtp server hostname |
| `smtp.username` | smtp authentication username |
| `smtp.password` | smtp authentication password |
| `smtp.from_address` | from email address |
| `smtp.ignore_cert_errors` | whether to ignore tls certificate errors |
| `smtp.modified_date` | smtp last modified datetime |

### stats

| variable | description |
| -- | -- |
| `stats.total` | total number of targets |
| `stats.sent` | number of emails sent |
| `stats.opened` | number of emails opened |
| `stats.clicked` | number of links clicked |
| `stats.submitted_data` | number of form submissions |
| `stats.email_reported` | number of reported emails |
| `stats.error` | number of delivery or processing errors |

### template

| variable | description |
| -- | -- |
| `template.id` | template id |
| `template.name` | template name |
| `template.envelope_sender` | sender display name |
| `template.subject` | email subject |
| `template.text` | email text body |
| `template.html` | email html body |
| `template.modified_date` | template last modified datetime |
