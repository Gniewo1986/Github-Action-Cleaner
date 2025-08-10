<!-- Improved compatibility of back to top link: See: https://github.com/othneildrew/Best-README-Template/pull/73 -->

<a id="readme-top"></a>

[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![project_license][license-shield]][license-url]

<br />
<div align="center">
  <a href="https://github.com/LoveDoLove/Github-Action-Cleaner">
    <img src="images/logo.png" alt="Logo" width="80" height="80">
  </a>

<h3 align="center">GitHub Action Cleaner</h3>

  <p align="center">
    Effortlessly clean up workflow runs in your GitHub repository with ready-to-use GitHub Actions.
    <br />
    <a href="https://github.com/LoveDoLove/Github-Action-Cleaner"><strong>Explore the docs »</strong></a>
    <br />
    <br />
    <a href="https://github.com/LoveDoLove/Github-Action-Cleaner">View Demo</a>
    &middot;
    <a href="https://github.com/LoveDoLove/Github-Action-Cleaner/issues/new?labels=bug&template=bug-report---.md">Report Bug</a>
    &middot;
    <a href="https://github.com/LoveDoLove/Github-Action-Cleaner/issues/new?labels=enhancement&template=feature-request---.md">Request Feature</a>
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
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgments">Acknowledgments</a></li>
  </ol>
</details>

<!-- ABOUT THE PROJECT -->

## About The Project

**GitHub Action Cleaner** helps you automatically delete old or failed workflow runs from your repository using simple, ready-to-use GitHub Actions workflows.  
No manual script setup or local execution is required—just copy the workflow YAML file to your repo and run it from the Actions tab.

**Features:**

- Delete all workflow runs except the current one.
- Delete up to 100 most recent failed workflow runs.
- No local setup or dependencies required.
- Secure: uses GitHub Actions tokens.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

### Built With

- [Python](https://www.python.org/)
- [GitHub Actions](https://docs.github.com/en/actions)

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- GETTING STARTED -->

## Getting Started

### Prerequisites

- A GitHub repository with Actions enabled.
- Repository admin or write access.

### Installation

1. Download one of the workflow files from this repository:
   - [`cleanup-all-runs.yml`](.github/workflows/cleanup-all-runs.yml): Deletes all workflow runs except the current one.
   - [`cleanup-failed-runs.yml`](.github/workflows/cleanup-failed-runs.yml): Deletes up to 100 most recent failed workflow runs.
2. Copy the file into your own repository at `.github/workflows/`.
3. Commit and push the changes.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- USAGE EXAMPLES -->

## Usage

1. Go to your repository's **Actions** tab.
2. Select the workflow you added (e.g., "Cleanup All Workflow Runs" or "Cleanup Failed Workflow Runs").
3. Click **Run workflow** to trigger the cleanup.

The workflow will automatically download and execute the latest cleanup script for you.

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

### Top contributors:

<a href="https://github.com/LoveDoLove/Github-Action-Cleaner/graphs/contributors">
  <img src="https://contrib.rocks/image?repo=LoveDoLove/Github-Action-Cleaner" alt="contrib.rocks image" />
</a>

<!-- LICENSE -->

## License

Distributed under the MIT License. See `LICENSE` for more information.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- CONTACT -->

## Contact

Project Link: [https://github.com/LoveDoLove/Github-Action-Cleaner](https://github.com/LoveDoLove/Github-Action-Cleaner)

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- ACKNOWLEDGMENTS -->

## Acknowledgments

- [Best-README-Template](https://github.com/othneildrew/Best-README-Template)
- [GitHub Actions Documentation](https://docs.github.com/en/actions)
- [Requests Library](https://docs.python-requests.org/)

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- MARKDOWN LINKS & IMAGES -->

[contributors-shield]: https://img.shields.io/github/contributors/LoveDoLove/Github-Action-Cleaner.svg?style=for-the-badge
[contributors-url]: https://github.com/LoveDoLove/Github-Action-Cleaner/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/LoveDoLove/Github-Action-Cleaner.svg?style=for-the-badge
[forks-url]: https://github.com/LoveDoLove/Github-Action-Cleaner/network/members
[stars-shield]: https://img.shields.io/github/stars/LoveDoLove/Github-Action-Cleaner.svg?style=for-the-badge
[stars-url]: https://github.com/LoveDoLove/Github-Action-Cleaner/stargazers
[issues-shield]: https://img.shields.io/github/issues/LoveDoLove/Github-Action-Cleaner.svg?style=for-the-badge
[issues-url]: https://github.com/LoveDoLove/Github-Action-Cleaner/issues
[license-shield]: https://img.shields.io/github/license/LoveDoLove/Github-Action-Cleaner.svg?style=for-the-badge
[license-url]: https://github.com/LoveDoLove/Github-Action-Cleaner/blob/main/LICENSE
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://linkedin.com/in/linkedin_username
[product-screenshot]: images/screenshot.png
