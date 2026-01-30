# Introduction

This project aims to be a text processor that treats the templates themselves as a working environment. To achieve this, the concepts of `functions` and `variables` have been introduced using an easy-to-follow syntax. The goal here, is to minimize the technical requirements needed for red teams to produce those _satisfying_ single-click reports during their engagements.

All the structures have been developed with expandability in mind. Feel free to add functionality through `modules`, and/or introduce support for common export `formats` such as `docx` or `xlsx`.

---

> [!NOTE]
> An immediate representation of the variables can be found in  `docs/variables.json`

| Type     | Signature / Name                     | Description                              |
| -------- | ------------------------------------ | ---------------------------------------- |
| Function | `{math.add: a, b}`                   | addition                                 |
| Function | `{math.sub: a, b}`                   | subtraction                              |
| Function | `{math.pct: a, b}`                   | percentage                               |
| Function | `{math.dif: a, b}`                   | absolute                                 |
| Function | `{text.upper: text}`                 | capitalizes first character only         |
| Function | `{text.lower: text}`                 | lowercases entire string                 |
| Function | `{text.ifnull: value, fallback}`     | fallback if value is null/empty          |
| Function | `{text.plural: n, singular, plural}` | singular/plural selection                |
| Function | `{date.format: date, format}`        | date formatting (strftime)               |
| Function | `{html.render: html}`                | HTML to markdown-safe output             |
| Variable | `id`                                 | campaign id                              |
| Variable | `name`                               | campaign name                            |
| Variable | `created_date`                       | campaign creation datetime               |
| Variable | `launch_date`                        | campaign launch datetime                 |
| Variable | `send_by_date`                       | campaign send-by datetime                |
| Variable | `completed_date`                     | campaign completion datetime             |
| Variable | `url`                                | campaign url                             |
| Variable | `status`                             | campaign status                          |
| Variable | `page.id`                            | landing page id                          |
| Variable | `page.name`                          | landing page name                        |
| Variable | `page.html`                          | landing page html content                |
| Variable | `page.capture_credentials`           | whether credentials are captured         |
| Variable | `page.capture_passwords`             | whether passwords are captured           |
| Variable | `page.redirect_url`                  | redirect url after submission            |
| Variable | `page.modified_date`                 | landing page last modified datetime      |
| Variable | `smtp.id`                            | smtp configuration id                    |
| Variable | `smtp.interface_type`                | smtp interface type                      |
| Variable | `smtp.name`                          | smtp display name                        |
| Variable | `smtp.host`                          | smtp server hostname                     |
| Variable | `smtp.username`                      | smtp authentication username             |
| Variable | `smtp.password`                      | smtp authentication password             |
| Variable | `smtp.from_address`                  | from email address                       |
| Variable | `smtp.ignore_cert_errors`            | whether to ignore tls certificate errors |
| Variable | `smtp.modified_date`                 | smtp last modified datetime              |
| Variable | `stats.total`                        | total number of targets                  |
| Variable | `stats.sent`                         | number of emails sent                    |
| Variable | `stats.opened`                       | number of emails opened                  |
| Variable | `stats.clicked`                      | number of links clicked                  |
| Variable | `stats.submitted_data`               | number of form submissions               |
| Variable | `stats.email_reported`               | number of reported emails                |
| Variable | `stats.error`                        | number of delivery or processing errors  |
| Variable | `template.id`                        | template id                              |
| Variable | `template.name`                      | template name                            |
| Variable | `template.envelope_sender`           | sender display name                      |
| Variable | `template.subject`                   | email subject                            |
| Variable | `template.text`                      | email text body                          |
| Variable | `template.html`                      | email html body                          |
| Variable | `template.modified_date`             | template last modified datetime          |
