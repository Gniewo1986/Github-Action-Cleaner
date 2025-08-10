<!-- Improved compatibility of back to top link: See: https://github.com/othneildrew/Best-README-Template/pull/73 -->

<a id="readme-top"></a>

[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![MIT License][license-shield]][license-url]

<br />
<div align="center">
  <a href="https://github.com/LoveDoLove/github-action-cleaner">
    <img src="images/logo.png" alt="Logo" width="80" height="80">
  </a>

<h3 align="center">GitHub Action Cleaner</h3>

  <p align="center">
    Automated workflows to clean up workflow runs in your GitHub repository.
    <br />
    <a href="https://github.com/LoveDoLove/github-action-cleaner"><strong>Explore the docs »</strong></a>
    <br />
    <br />
    <a href="https://github.com/LoveDoLove/github-action-cleaner">View Demo</a>
    &middot;
    <a href="https://github.com/LoveDoLove/github-action-cleaner/issues/new?labels=bug&template=bug-report---.md">Report Bug</a>
    &middot;
    <a href="https://github.com/LoveDoLove/github-action-cleaner/issues/new?labels=enhancement&template=feature-request---.md">Request Feature</a>
  </p>
</div>

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

## About The Project

GitHub Action Cleaner provides reusable GitHub Actions workflows to help you keep your repository clean by deleting old or failed workflow runs. This is especially useful for repositories with frequent CI/CD runs, helping you save storage and maintain a tidy Actions history.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

### Built With

- [GitHub Actions](https://docs.github.com/en/actions)
- [actions/github-script](https://github.com/actions/github-script)

<p align="right">(<a href="#readme-top">back to top</a>)</p>

## Getting Started

To use these workflows in your own repository, follow the steps below.

### Prerequisites

- A GitHub repository where you have admin or workflow permissions.

### Installation

1. Copy the desired workflow YAML file(s) from the `workflows/` directory into your repository's `.github/workflows/` directory.
2. Optionally, update the workflow name or schedule as needed.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

## Usage

### Delete All Workflow Runs

This workflow deletes all workflow runs in the repository except the current run.  
To trigger manually:

- Go to the "Actions" tab in your repository.
- Select "Delete All Workflow Runs".
- Click "Run workflow".

### Delete Failed Workflow Runs

This workflow deletes only failed workflow runs (up to the 100 most recent completed runs).  
To trigger manually:

- Go to the "Actions" tab in your repository.
- Select "Delete Failed Workflow Runs".
- Click "Run workflow".

_Ensure you have appropriate permissions, as these workflows require `actions: write` permission._

<p align="right">(<a href="#readme-top">back to top</a>)</p>

## Roadmap

- [x] Delete all workflow runs
- [x] Delete failed workflow runs
- [ ] Add scheduled cleanup support
- [ ] Add configuration for run retention

See the [open issues](https://github.com/LoveDoLove/github-action-cleaner/issues) for a full list of proposed features (and known issues).

<p align="right">(<a href="#readme-top">back to top</a>)</p>

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

<a href="https://github.com/LoveDoLove/github-action-cleaner/graphs/contributors">
  <img src="https://contrib.rocks/image?repo=LoveDoLove/github-action-cleaner" alt="contrib.rocks image" />
</a>

## License

Distributed under the MIT License. See `LICENSE` for more information.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

## Contact

Your Name - [@twitter_handle](https://twitter.com/twitter_handle) - email@email_client.com

Project Link: [https://github.com/LoveDoLove/github-action-cleaner](https://github.com/LoveDoLove/github-action-cleaner)

<p align="right">(<a href="#readme-top">back to top</a>)</p>

## Acknowledgments

- [actions/github-script](https://github.com/actions/github-script)
- [GitHub Actions Documentation](https://docs.github.com/en/actions)
- [Best README Template](https://github.com/othneildrew/Best-README-Template)

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- MARKDOWN LINKS & IMAGES -->

[contributors-shield]: https://img.shields.io/github/contributors/LoveDoLove/github-action-cleaner.svg?style=for-the-badge
[contributors-url]: https://github.com/LoveDoLove/github-action-cleaner/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/LoveDoLove/github-action-cleaner.svg?style=for-the-badge
[forks-url]: https://github.com/LoveDoLove/github-action-cleaner/network/members
[stars-shield]: https://img.shields.io/github/stars/LoveDoLove/github-action-cleaner.svg?style=for-the-badge
[stars-url]: https://github.com/LoveDoLove/github-action-cleaner/stargazers
[issues-shield]: https://img.shields.io/github/issues/LoveDoLove/github-action-cleaner.svg?style=for-the-badge
[issues-url]: https://github.com/LoveDoLove/github-action-cleaner/issues
[license-shield]: https://img.shields.io/github/license/LoveDoLove/github-action-cleaner.svg?style=for-the-badge
[license-url]: https://github.com/LoveDoLove/github-action-cleaner/blob/master/LICENSE
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://linkedin.com/in/linkedin_username
[product-screenshot]: images/logo.png
