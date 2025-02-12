# Scientific Python Lectures translations

![All Contributors](https://img.shields.io/github/all-contributors/tkoyama010/scientific-python-lectures-translations?color=ee8449)

[scientific-python-lectures official documentation translations](https://github.com/tkoyama010/scientific-python-lectures-translations) is a project to provide scientific-python-lectures official documentation, hosted on
the Read The Docs platform, in multiple languages.

> [!NOTE]
> This is following [PEP 545 – Python Documentation Translations](https://peps.python.org/pep-0545/).

> [!NOTE]
> The current procedure is bit tricky because Read The Docs
> doesn't have a way to specify options for `sphinx-build` command.
> **conf.py** files for each languages have `language` and `locale_dirs`
> values without having full copy of **conf.py** of scientific-python-lectures doc. If we want
> to specify **conf.py** file that is out of source directory, we will use
> `-c` option for the `sphinx-build` command. Unfortunately Read the Docs
> doesn't support that. If there is a better way, open an issue.

## How the translated documentation projects are setup on RTD

Instructions:
https://docs.readthedocs.org/en/latest/localization.html#project-with-multiple-translations

Key points:

- There is a RTD project for each language.
- Each project needs the correct **Language** setting on the
  **Settings** page.
- The parent project needs connections created to each translated
  project on the **Translations Settings** page.

| Language | Build Status                                                                                                                                                                                  | RTD Project                                                                                                                                    | Transifex                                                                                                                                               |
| :------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 日本語   | [![Documentation Status](https://readthedocs.org/projects/scientific-python-lectures-ja/badge/?version=latest)](https://scientific-python-lectures-ja.readthedocs.io/ja/latest/?badge=latest) | [![readthedocs.org](https://img.shields.io/badge/readthedocs-ja-ff7964.svg?)](https://readthedocs.org/projects/scientific-python-lectures-ja/) | [![Transifex](https://img.shields.io/badge/Transifex-ja-blue.svg?)](https://app.transifex.com/tkoyama010/scientific-python-lectures-doc/translate/#/ja) |

## How to add a new language translation

1.  Add new language to `locale/update.sh`:

```diff
-   rm -R es ja
-   tx pull -l es,ja
+   rm -R es ja pt_BR
+   tx pull -l es,ja,pt_BR
```

2.  Update po files:

```
sh ./locale/update.sh
```

3.  Commit them

4.  Add new project on Read The Docs. For example, for `pt_BR`:

    https://readthedocs.org/projects/scientific-python-lectures-pt-br/

> [!NOTE]
> If a RTD project name for a translation is already taken,
> create a unique project name instead. For example, when `scientific-python-lectures-ru`
> was taken, `scientific-python-lectures-doc-ru` was used instead.

5.  Add new translation project to parent project:

    https://readthedocs.org/dashboard/scientific-python-lectures/translations/

## Contributors ✨

Thanks goes to these wonderful people ([emoji key](https://allcontributors.org/docs/en/emoji-key)):

<!-- ALL-CONTRIBUTORS-LIST:START - Do not remove or modify this section -->
<!-- prettier-ignore-start -->
<!-- markdownlint-disable -->
<table>
  <tbody>
    <tr>
      <td align="center" valign="top" width="14.28%"><a href="https://github.com/tkoyama010"><img src="https://avatars.githubusercontent.com/u/7513610?v=4?s=100" width="100px;" alt="Tetsuo Koyama"/><br /><sub><b>Tetsuo Koyama</b></sub></a><br /><a href="https://github.com/tkoyama010/scientific-python-lectures-translations/commits?author=tkoyama010" title="Documentation">📖</a> <a href="#infra-tkoyama010" title="Infrastructure (Hosting, Build-Tools, etc)">🚇</a> <a href="#translation-tkoyama010" title="Translation">🌍</a> <a href="#ideas-tkoyama010" title="Ideas, Planning, & Feedback">🤔</a> <a href="#maintenance-tkoyama010" title="Maintenance">🚧</a> <a href="https://github.com/tkoyama010/scientific-python-lectures-translations/pulls?q=is%3Apr+reviewed-by%3Atkoyama010" title="Reviewed Pull Requests">👀</a></td>
      <td align="center" valign="top" width="14.28%"><a href="https://pre-commit.ci"><img src="https://avatars.githubusercontent.com/u/64617429?v=4?s=100" width="100px;" alt="pre-commit.ci"/><br /><sub><b>pre-commit.ci</b></sub></a><br /><a href="#maintenance-pre-commit-ci" title="Maintenance">🚧</a></td>
    </tr>
  </tbody>
</table>

<!-- markdownlint-restore -->
<!-- prettier-ignore-end -->

<!-- ALL-CONTRIBUTORS-LIST:END -->

This project follows the [all-contributors](https://github.com/all-contributors/all-contributors) specification. Contributions of any kind welcome!
