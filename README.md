# TrackRules

Small tool to help you stay on the track with Track&amp;Field rules.

## Rationale

[World Athletic rule books](https://www.worldathletics.org/about-iaaf/documents/book-of-rules)
updates in irregular way, also there is no alternative way to get all of those documents updated
than check and click all of those documents.

## How it works?

TrackRules searches for rule books and simply downloads it.

## Prerequisites

- Trackrules uses Selenium with Google Chrome web browser, hence download
  [chromium web driver](https://chromedriver.chromium.org/) with correlated version to your chrome version.
  Add chromedriver into your `PATH` environment variable.
- Python environment

## Roadmap / Things to do

CI/CD

- Automate linting
- Automate checks with python versions

Upgrades

- Use TrackRules in CLI, to be able to use in automate way
- Compare and update only necessary documents
