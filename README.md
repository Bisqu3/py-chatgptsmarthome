<!-- Improved compatibility of back to top link: See: https://github.com/othneildrew/Best-README-Template/pull/73 -->
<a name="readme-top"></a>
<!--
*** Thanks for checking out the Best-README-Template. If you have a suggestion
*** that would make this better, please fork the repo and create a pull request
*** or simply open an issue with the tag "enhancement".
*** Don't forget to give the project a star!
*** Thanks again! Now go create something AMAZING! :D
-->



<!-- PROJECT SHIELDS -->
<!--
*** I'm using markdown "reference style" links for readability.
*** Reference links are enclosed in brackets [ ] instead of parentheses ( ).
*** See the bottom of this document for the declaration of the reference variables
*** for contributors-url, forks-url, etc. This is an optional, concise syntax you may use.
*** https://www.markdownguide.org/basic-syntax/#reference-style-links
-->
[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![MIT License][license-shield]][license-url]
[![LinkedIn][linkedin-shield]][linkedin-url]



<!-- PROJECT LOGO -->
<br />
<div align="center">
  <a href="https://github.com/Bisqu3/chatgptcontrol">
    <img src="logo.png" alt="Logo" width="80" height="80">
  </a>

<h3 align="center">ChatGPT Smart Home Assistant</h3>

  <p align="center">
    Speech to text with Google Cloud to converse with ChatGPT using OpenAIs API library.
    Distinguishes Smart home commands from normal conversation.
    There is no activation word, if your mic is on the assistant is listening.
    <br />
    <a href="https://github.com/Bisqu3/chatgptcontrol"><strong>Explore the docs »</strong></a>
    <br />
    <br />
    <a href="https://github.com/Bisqu3/chatgptcontrol">View Demo</a>
    ·
    <a href="https://github.com/Bisqu3/chatgptcontrol/issues">Report Bug</a>
    ·
    <a href="https://github.com/Bisqu3/chatgptcontrol/issues">Request Feature</a>
  </p>
</div>



<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgments">Acknowledgments</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project

[![Product Name Screen Shot][product-screenshot]](https://example.com)

Made in linux. audio tested on windows 10.

<p align="right">(<a href="#readme-top">back to top</a>)</p>



### Built With

OpenAI
Google Cloud
PYaudio
pyttsx3
phue

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- GETTING STARTED -->
## Getting Started
Only works with Phillips Hue Bridge.
Must provide your own keys for the OpenAI and Google Cloud APIs

### Prerequisites

* download python libraries
  ```sh
  pip install pyaudio google.cloud pyttsx3 openai phue
  ```

### Installation

1. Setup your OpenAI and Google Cloud API's [OPENAI](https://openai.com/blog/openai-api) [GOOGLE CLOUD](https://cloud.google.com/speech-to-text?utm_source=google&utm_medium=cpc&utm_campaign=na-US-all-en-dr-bkws-all-all-trial-b-dr-1605212&utm_content=text-ad-none-any-DEV_c-CRE_648329034713-ADGP_Desk%20%7C%20BKWS%20-%20BRO%20%7C%20Txt%20_%20AI%20%26%20ML%20_%20Speech-to-Text_General_Speech%20Recognition%20Google%20Cloud-KWID_43700075187123884-kwd-914125495112&utm_term=KW_google%20cloud%20speech%20recognition-ST_google%20cloud%20speech%20recognition&gclid=CjwKCAjwhdWkBhBZEiwA1ibLmLU6NZt2MqurXFKMJO0a_NkEdb_eaFLTwFadGxD3KIv3bZBpUPB77BoCBKUQAvD_BwE&gclsrc=aw.ds](https://cloud.google.com/speech-to-text?utm_source=google&utm_medium=cpc&utm_campaign=na-US-all-en-dr-bkws-all-all-trial-b-dr-1605212&utm_content=text-ad-none-any-DEV_c-CRE_648329034665-ADGP_Desk%20%7C%20BKWS%20-%20BRO%20%7C%20Txt%20_%20AI%20%26%20ML%20_%20Speech-to-Text_Converter%20Audio%20to%20Text%20GCP-KWID_43700075187123533-kwd-1720635562699&utm_term=KW_gcp%20audio%20to%20text%20converter%20online-ST_gcp%20audio%20to%20text%20converter%20online&gclid=Cj0KCQjwqNqkBhDlARIsAFaxvwzK1ef_29WXJM_opshLMpT-rSyAUqzmsNu3YQ8ZFLJ5KlAsp84iGMMaAiNsEALw_wcB&gclsrc=aw.ds))
2. Clone the repo
   ```sh
   git clone https://github.com/Bisqu3/chatgptcontrol.git
   ```
3. Install dependencies
   ```sh
   pip install pyaudio google.cloud pyttsx3 openai phue
   ```
4. Enter your OPENAI API in `configure.py`
   ```py
   API_OPENAI = 'ENTER YOUR API';
   ```
5. Put your Google Cloud JSON authentication file in the keys folder.
   Rename it to auth.js
6. run runstt.py for speech recognition or type.py
   ```sh
   python runstt.py
   ``` 
<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- USAGE EXAMPLES -->
## Usage

In lightcontrol.py
create a room with a lower case name. the lights are the same name as the philips hue app.
```py
livingroom = ['Light1','Light2',...]
```

To pair the app to your bridge, hit the pair button before inputting your first smart home request.

When you say
"Turn off living room lights"
it will be split into
```py 
lights("livingroom", 0)
```
_For more examples, please refer to the [Documentation](https://example.com)_

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- ROADMAP -->
## Roadmap

- [ ] Google Cloud TSS (to replace pyttsx3)
- [ ] More smart home functionality
- [ ] Long term memory / optional activation word.
    - [ ] Flask Web App for ease of use

See the [open issues](https://github.com/Bisqu3/chatgptcontrol/issues) for a full list of proposed features (and known issues).

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- CONTRIBUTING -->
## Contributing

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement".
Don't forget to give the project a star! Thanks again!

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE.txt` for more information.

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- CONTACT -->
## Contact

Nicholas Nielsen - [@twitter_handle](https://twitter.com/twitter_handle) - nicknielsen5@gmail.com

Project Link: [https://github.com/Bisqu3/chatgptcontrol](https://github.com/Bisqu3/chatgptcontrol)

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- ACKNOWLEDGMENTS -->
## Acknowledgments

* [Nicholas Nielsen for V1 work](https://github.com/Bisqu3)
* []()
* []()

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/Bisqu3/chatgptcontrol.svg?style=for-the-badge
[contributors-url]: https://github.com/Bisqu3/chatgptcontrol/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/Bisqu3/chatgptcontrol.svg?style=for-the-badge
[forks-url]: https://github.com/Bisqu3/chatgptcontrol/network/members
[stars-shield]: https://img.shields.io/github/stars/Bisqu3/chatgptcontrol.svg?style=for-the-badge
[stars-url]: https://github.com/Bisqu3/chatgptcontrol/stargazers
[issues-shield]: https://img.shields.io/github/issues/Bisqu3/chatgptcontrol.svg?style=for-the-badge
[issues-url]: https://github.com/Bisqu3/chatgptcontrol/issues
[license-shield]: https://img.shields.io/github/license/Bisqu3/chatgptcontrol.svg?style=for-the-badge
[license-url]: https://github.com/Bisqu3/chatgptcontrol/blob/master/LICENSE.txt
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://linkedin.com/in/linkedin_username
[product-screenshot]: images/screenshot.png
[Next.js]: https://img.shields.io/badge/next.js-000000?style=for-the-badge&logo=nextdotjs&logoColor=white
[Next-url]: https://nextjs.org/
[React.js]: https://img.shields.io/badge/React-20232A?style=for-the-badge&logo=react&logoColor=61DAFB
[React-url]: https://reactjs.org/
[Vue.js]: https://img.shields.io/badge/Vue.js-35495E?style=for-the-badge&logo=vuedotjs&logoColor=4FC08D
[Vue-url]: https://vuejs.org/
[Angular.io]: https://img.shields.io/badge/Angular-DD0031?style=for-the-badge&logo=angular&logoColor=white
[Angular-url]: https://angular.io/
[Svelte.dev]: https://img.shields.io/badge/Svelte-4A4A55?style=for-the-badge&logo=svelte&logoColor=FF3E00
[Svelte-url]: https://svelte.dev/
[Laravel.com]: https://img.shields.io/badge/Laravel-FF2D20?style=for-the-badge&logo=laravel&logoColor=white
[Laravel-url]: https://laravel.com
[Bootstrap.com]: https://img.shields.io/badge/Bootstrap-563D7C?style=for-the-badge&logo=bootstrap&logoColor=white
[Bootstrap-url]: https://getbootstrap.com
[JQuery.com]: https://img.shields.io/badge/jQuery-0769AD?style=for-the-badge&logo=jquery&logoColor=white
[JQuery-url]: https://jquery.com 
