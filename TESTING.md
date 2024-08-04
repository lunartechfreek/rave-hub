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

## Browser Compatibility

I've tested my deployed project on multiple browsers to check for compatibility issues.

### Browser Testing

| Browser | Home | Notes |
| --- | --- | --- |
| Chrome | ![Chrome Browser](documentation/browser-testing/browser-chrome.png) | Works as expected |
| Edge | ![Edge Browser](documentation/browser-testing/browser-edge.png) | Works as expected |
| Firefox | ![Firefox Browser](documentation/browser-testing/browser-firefox.png) | Works as expected |
| Opera | ![Opera Browser](documentation/browser-testing/browser-opera.png) | Works as expected |
| Safari | ![Safari Browser](documentation/browser-testing/browser-safari.png) | Works as expected |

### Device Browser Testing

| Device | Browser | Home | Notes |
| --- | --- | --- | --- |
| Iphone 15 ProMax | Safari | ![Iphone 15 ProMax](documentation/device-testing/mobile-iphone-15-promax-safari.PNG) | Works as expected - Manual test |
| Iphone 13 ProMax | Safari | ![Iphone 13 ProMax](documentation/responsiveness/mobile-iphone-13-promax-safari.png) | Works as expected |
| Iphone 12 Pro | Chrome | ![Iphone 12 Pro](documentation/device-testing/mobile-iphone-12-pro-chrome.png) | Works as expected |
| Samsung Galaxy S22 Ultra | Chrome | ![Samsung Galaxy S22 Ultra](documentation/device-testing/mobile-samsung-galaxy-s22-ultra-chrome.png) | Works as expected - Manual test |
| Google Pixel 8 Pro | Edge | ![Pixel 8 Pro](documentation/device-testing/mobile-google-pixel-8-pro-edge.png) | Works as expected |
| Google Pixel 7 | Chrome | ![Pixel 7](documentation/device-testing/mobile-google-pixel-7-chrome.png) | Works as expected |
| Huawei P30 | Chrome | ![Huawei P30](documentation/device-testing/mobile-huawei-p30-chrome.png) | Works as expected |
| Samsung Tab S7 | Firefox | ![Samsung Tab 7](documentation/device-testing/tablet-samsung-tab-s7-firefox.png) | Works as expected |
| Ipad 10th Gen | Safari | ![Ipad 10th Gen](documentation/responsiveness/tablet-ipad-10-safari.png) | Works as expected |

## Responsiveness

I've tested my deployed project on multiple devices to check for responsiveness issues.

| Device | Home | Notes | Test |
| --- | --- | --- | --- |
| Iphone 15 ProMax | ![Iphone 15 ProMax](documentation/responsiveness/iphone-15-promax-safari.PNG) | Works as expected | Manual test |
| Iphone 13 ProMax | ![Iphone 13 ProMax](documentation/responsiveness/mobile-iphone-13-promax-safari.png) | Works as expected | Browserstack test |
| Iphone 12 Pro | ![Iphone 12 Pro](documentation/responsiveness/iphone-12-pro-chrome.png) | Works as expected | Browserstack test |
| Iphone SE | ![Iphone SE](documentation/responsiveness/iphone-se-dev.png) | Works as expected | Chrome DevTools test |
| Iphone XR | ![Iphone XR](documentation/responsiveness/iphone-xr-dev.png) | Works as expected | Chrome DevTools test |
| Samsung Galaxy S22 Ultra | ![Samsung Galaxy S22 Ultra](documentation/responsiveness/mobile-samsung-galaxy-s22-ultra-chrome.png) | Works as expected | Manual test |
| Google Pixel 8 Pro | ![Pixel 8 Pro](documentation/responsiveness/mobile-google-pixel-8-pro-edge.png) | Works as expected | Browserstack test |
| Google Pixel 7 | ![Pixel 7](documentation/responsiveness/mobile-google-pixel-7-chrome.png) | Works as expected | Browserstack test |
| Samsung Galaxy Z Fold 5 | ![Galaxy Z](documentation/responsiveness/galaxy-z-dev.png) | Works as expected | Chrome DevTools test |
| Samsung Galaxy S8+ | ![Samsung Galaxy S8+](documentation/responsiveness/galaxy-s8-dev.png) | Works as expected | Chrome DevTools test |
| Samsung Galaxy S20 Ultra | ![Samsung Galaxy S20 Ultra](documentation/responsiveness/galaxy-s20-ultra-dev.png) | Works as expected | Chrome DevTools test |
| Samsung Galaxy A51/71 | ![Samsung Galaxy A51/71](documentation/responsiveness/galaxy-a51-71-dev.png) | Works as expected | Chrome DevTools test |
| Huawei P30 | ![Huawei P30](documentation/responsiveness/mobile-huawei-p30-chrome.png) | Works as expected | Browserstack test |
| Samsung Tab S7 | Firefox | ![Samsung Tab 7](documentation/responsiveness/tablet-samsung-tab-s7-firefox.png) | Works as expected |
| Ipad 10th Gen | ![Ipad 10th Gen](documentation/responsiveness/tablet-ipad-10-safari.png) | Works as expected | Browserstack test |
| Ipad Air | ![Ipad Air](documentation/responsiveness/ipad-air-dev.png) | Works as expected | Chrome DevTools test |
| Ipad Mini | ![Ipad Mini](documentation/responsiveness/ipad-mini-dev.png) | Works as expected | Chrome DevTools test |
| Microsoft Surface Duo | ![Microsoft Surface Duo](documentation/responsiveness/surface-duo-dev.png) | Works as expected | Chrome DevTools test |
| Microsoft Surface Pro 7 | ![Microsoft Surface Pro 7](documentation/responsiveness/surface-pro-7-dev.png) | Works as expected | Chrome DevTools test |


## Lighthouse Audit

I've tested my deployed project using the Lighthouse Audit tool to check for any major issues.

| Page | Mobile | Desktop | Notes |
| --- | --- | --- | --- |
| Index | ![screenshot](documentation/lighthouse/desktop-index.png) | ![screenshot](documentation/lighthouse/mobile-index.png) |  |
| Add Festival | ![screenshot](documentation/lighthouse/desktop-add-festival.png) | ![screenshot](documentation/lighthouse/mobile-add-festival.png) |  |
| Edit Festival | ![screenshot](documentation/lighthouse/desktop-edit-festival.png) | ![screenshot](documentation/lighthouse/mobile-edit-festival.png) | ![screenshot](documentation/lighthouse/contrast-error.png)I think that the error is being caused by the fact that this is the only page that renders the background as the image that the user has uploaded. I have manually checked the contrast of the text items as is shown below and the accessibility is passing. This is something that will be listed as a future devolpment to look further into ![screenshot](documentation/lighthouse/contrast1.png) ![screenshot](documentation/lighthouse/contrast2.png) |
| Festival Detail | ![screenshot](documentation/lighthouse/desktop-festival-detail.png) | ![screenshot](documentation/lighthouse/mobile-festival-detail.png) |  |
| Festival List | ![screenshot](documentation/lighthouse/desktop-festival-list.png) | ![screenshot](documentation/lighthouse/mobile-festival-list.png) |  |
| Festival Search | ![screenshot](documentation/lighthouse/desktop-festival-search.png) | ![screenshot](documentation/lighthouse/mobile-festival-search.png) |  |
| User Profile | ![screenshot](documentation/lighthouse/desktop-user-profile.png) | ![screenshot](documentation/lighthouse/mobile-user-profile.png) |  |
| About | ![screenshot](documentation/lighthouse/desktop-about.png) | ![screenshot](documentation/lighthouse/mobile-about.png) |  |
| Contact | ![screenshot](documentation/lighthouse/desktop-contact-us.png) | ![screenshot](documentation/lighthouse/mobile-contact-us.png) |  |
| Login | ![screenshot](documentation/lighthouse/desktop-login.png) | ![screenshot](documentation/lighthouse/mobile-login.png) |  |
| Sign Up | ![screenshot](documentation/lighthouse/desktop-signup.png) | ![screenshot](documentation/lighthouse/mobile-signup.png) |  |
| Logout | ![screenshot](documentation/lighthouse/desktop-logout.png) | ![screenshot](documentation/lighthouse/mobile-logout.png) |  |
| Password Change | ![screenshot](documentation/lighthouse/desktop-password-change.png) | ![screenshot](documentation/lighthouse/mobile-password-change.png) |  |
| 404 | ![screenshot](documentation/lighthouse/desktop-404.png) | ![screenshot](documentation/lighthouse/mobile-404.png) |  |
| 505 | ![screenshot](documentation/lighthouse/desktop-500.png) | ![screenshot](documentation/lighthouse/mobile-500.png) |  |


