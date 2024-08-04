# Testing

> Return back to the [README.md](README.md) file.

## Code Validation

### HTML

I have used the recommended [HTML W3C Validator](https://validator.w3.org) to validate all of my HTML files.

| Directory | File | Screenshot | Notes |
| --- | --- | --- | --- |
| event | add_festival.html | ![screenshot](documentation/validation/add-festival.png) | Passed with no errors |
| event | edit_festival.html | ![screenshot](documentation/validation/edit-festival.png) | Passed with no errors |
| event | festival_detail.html | ![screenshot](documentation/validation/festival-detail.png) | Passed with no errors |
| event | festival_list.html | ![screenshot](documentation/validation/festival-list.png) | Passed with no errors |
| event | festival_search.html | ![screenshot](documentation/validation/festival-search.png) | Passed with no errors |
| event | index.html | ![screenshot](documentation/validation/index.png) | Passed with no errors |
| event | user_profile.html | ![screenshot](documentation/validation/user-profile.png) | Passed with no errors |
| information | about.html | ![screenshot](documentation/validation/about.png) | Passed with no errors |
| information | contact_us.html | ![screenshot](documentation/validation/contact-us.png) | Passed with no errors |
| account | login.html | ![screenshot](documentation/validation/login.png) | Passed with no errors |
| account | signup.html | ![screenshot](documentation/validation/signup.png) | Passed with no errors |
| account | logout.html | ![screenshot](documentation/validation/logout.png) | Passed with no errors |
| account | password_change.html | ![screenshot](documentation/validation/password-change.png) | Note due to allauth rendering a trailing forward slash |
| | | ![screenshot](documentation/validation/password-change-note.png) | Searched for issue noted on page source but it says the line causing the issue doesn't exist |
| templates | 404.html | ![screenshot](documentation/validation/404.png) | Passed with no errors, done by text input due to it not being able to check it through direct input with it being an error page |
| templates | 500.html | ![screenshot](documentation/validation/500.png) | Passed with no errors, done by text input due to it not being able to check it through direct input with it being an error page |

### CSS

I have used the recommended [CSS Jigsaw Validator](https://jigsaw.w3.org/css-validator) to validate all of my CSS files.

| Directory | File | Screenshot | Notes |
| --- | --- | --- | --- |
| static | style.css | ![screenshot](documentation/validation/jigsaw.png) | Passed with no errors |

### Python

I have used the recommended [PEP8 CI Python Linter](https://pep8ci.herokuapp.com) to validate all of my Python files.

| Directory | File | CI URL | Screenshot | Notes |
| --- | --- | --- | --- | --- |
| event | admin.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/lunartechfreek/rave-hub/main/event/admin.py) | ![screenshot](documentation/validation/event-admin.png) | Passed with no errors |
| event | forms.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/lunartechfreek/rave-hub/main/event/forms.py) | ![screenshot](documentation/validation/event-forms.png) | Passed with no errors |
| event | models.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/lunartechfreek/rave-hub/main/event/models.py) | ![screenshot](documentation/validation/event-models.png) | Passed with no errors |
| event | urls.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/lunartechfreek/rave-hub/main/event/urls.py) | ![screenshot](documentation/validation/event-urls.png) | Passed with no errors |
| event | views.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/lunartechfreek/rave-hub/main/event/views.py) | ![screenshot](documentation/validation/event-views.png) | Passed with no errors |
| information | admin.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/lunartechfreek/rave-hub/main/information/admin.py) | ![screenshot](documentation/validation/info-admin.png) | Passed with no errors |
| information | forms.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/lunartechfreek/rave-hub/main/information/forms.py) | ![screenshot](documentation/validation/info-forms.png) | Passed with no errors |
| information | models.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/lunartechfreek/rave-hub/main/information/models.py) | ![screenshot](documentation/validation/info-models.png) | Passed with no errors |
| information | urls.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/lunartechfreek/rave-hub/main/information/urls.py) | ![screenshot](documentation/validation/info-urls.png) | Passed with no errors |
| information | views.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/lunartechfreek/rave-hub/main/information/views.py) | ![screenshot](documentation/validation/info-views.png) | Passed with no errors |
|  | manage.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/lunartechfreek/rave-hub/main/manage.py) | ![screenshot](documentation/validation/manage.png) | Passed with no errors |
| ravehub | settings.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/lunartechfreek/rave-hub/main/ravehub/settings.py) | ![screenshot](documentation/validation/ravehub-settings.png) | Passed with no errors |
| ravehub | urls.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/lunartechfreek/rave-hub/main/ravehub/urls.py) | ![screenshot](documentation/validation/ravehub-urls.png) | Passed with no errors |
| ravehub | views.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/lunartechfreek/rave-hub/main/ravehub/views.py) | ![screenshot](documentation/validation/ravehub-views.png) | Passed with no errors |

