# Digital Tools for Finance

Course taught at the University of Zurich in Fall 2021 by Igor Pozdeev.
This repository is based on the [digital-tools-for-finance](https://github.com/ipozdeev/digital-tools-for-finance) repository.

## Setup the environment
As part of the data management you need to set the research data path.
Please create a `.env` file with the following content:

```env
RESEARCH_DATA_PATH = "Path to your research"
FRED_KEY = "Your FRED key"
```

## Assignment
hosted as a single repository on Github;

- Repository is hosten on GitHub under [dtff-group-project](https://github.com/mxjweb/dtff-group-project).

having a well defined and concise structure;

- Structure is similar to the course structure

having a history of commits and merges;

- Commits can be seen [here](https://github.com/mxjweb/dtff-group-project/commits/master).

boasting a database with an API and possibility to update data;

- API and data can be found under [Assignment/Api](00-Assignment/api/).

featuring a paper (does not have to be of meaningful content) written in LaTeX, with sections, a table of contents, tables and figures where figures adhere to the visualization standards discussed in the corresponding lectures;

- Paper is under [Assignment/Text/Paper](00-Assignment/text/paper).

featuring a beamer presentation (does not have to be of meaningful content though) written in LaTeX, with sections, a table of contents, tables and figures where figures adhere to the visualization standards discussed in the corresponding lectures;

- Beamer presentation is under [Assignment/Text/Presentation](00-Assignment/text/presentation).

(optional) with one interactive app or jupyter Notebook presenting some findings (or some meaningless data, e.g. the histogram of Laplace distribution).

- Shiny app and Jupyter Notebook can be found under [Assignment/Jupyter](00-Assignment/jupyter/) and [Assignment/Shiny](00-Assignment/shiny/). Original code and article for the Shiny App can be be found [here](https://towardsdatascience.com/monitoring-stock-performance-made-easy-with-r-and-shiny-b6ab5fb02085).
