{
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {},
      "source": [
        "---\n",
        "title: \"Client Report - [Insert Project Title]\"\n",
        "subtitle: \"Course DS 250\"\n",
        "author: \"[STUDENT NAME]\"\n",
        "format:\n",
        "  html:\n",
        "    self-contained: true\n",
        "    page-layout: full\n",
        "    title-block-banner: true\n",
        "    toc: true\n",
        "    toc-depth: 3\n",
        "    toc-location: body\n",
        "    number-sections: false\n",
        "    html-math-method: katex\n",
        "    code-fold: true\n",
        "    code-summary: \"Show the code\"\n",
        "    code-overflow: wrap\n",
        "    code-copy: hover\n",
        "    code-tools:\n",
        "        source: false\n",
        "        toggle: true\n",
        "        caption: See code\n",
        "execute: \n",
        "  warning: false\n",
        "    \n",
        "---\n",
        "\n",
        "\n",
        "_THIS `.qmd` IS INSTRUCTIONAL AND SHOULD `NOT` BE USED TO WRITE YOUR REPORTS (EXCEPTION - PROJECT 0). THERE IS ANOTHER TEMPLATE FILE FOR THAT. YOU WILL NEED TO `PREVIEW` THE REPORT TO PRODUCE A `.html` FILE. YOU WILL SUBMIT THE `.html` FILE ON CANVAS._\n"
      ],
      "id": "5fa6051e"
    },
    {
      "cell_type": "code",
      "metadata": {},
      "source": [
        "#| label: libraries\n",
        "#| include: false\n",
        "import pandas as pd\n",
        "import numpy as np\n",
        "from lets_plot import *\n",
        "\n",
        "LetsPlot.setup_html()"
      ],
      "id": "libraries",
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "metadata": {},
      "source": [
        "## Elevator pitch\n",
        "_A SHORT (2-3 SENTENCES) PARAGRAPH THAT `DESCRIBES KEY INSIGHTS` TAKEN FROM METRICS IN THE PROJECT RESULTS THINK TOP OR MOST IMPORTANT RESULTS._ (Note: this is not a summary of the project, but a summary of the results.)\n",
        "\n",
        "_A Client has requested this analysis and this is your one shot of what you would say to your boss in a 2 min elevator ride before he takes your report and hands it to the client._\n"
      ],
      "id": "12adfc74"
    },
    {
      "cell_type": "code",
      "metadata": {},
      "source": [
        "#| label: project-data\n",
        "#| code-summary: Read and format project data\n",
        "\n",
        "# Learn morea about Code Cells: https://quarto.org/docs/reference/cells/cells-jupyter.html\n",
        "\n",
        "# Include and execute your code here\n",
        "df = pd.read_csv(\"https://raw.githubusercontent.com/byuidatascience/data4python4ds/master/data-raw/mpg/mpg.csv\")"
      ],
      "id": "project-data",
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "metadata": {},
      "source": [
        "__Highlight the Questions and Tasks__\n",
        "\n",
        "## Question|Task 1\n",
        "\n",
        "__COPY PASTE QUESTION|TASK 1 FROM THE PROJECT HERE__\n",
        "\n",
        "_Add details here to answer the question but `NOT` like an assignment Q&A. You need to `write your answers as a consulting solution report`. A Client needs to understand the answer, but also needs to understand the decisions that went into the answer (when applicable)._\n",
        "\n",
        "_include figures in chunks and discuss your findings in the figure._\n",
        "\n",
        "- _YOU SHOULD HAVE QUALITY WRITING THAT DESCRIBES YOUR CHARTS AND TABLES._\n",
        "\n",
        "- _WE HIGHLY RECOMMEND [GRAMMARLY](https://grammarly.com/) TO FIX YOUR SPELLING AND GRAMMAR. WRITING TAKES TIME TO BE CLEAR. SPEND THE TIME TO PRACITCE._ \n",
        "\n",
        "- _YOU SHOULD HAVE QUALITY COMMENTS THAT DESCRIBES YOUR CODES. OFTEN CODEERS WORK IN TEAMS AND YOU NEED TO HAVE QUALTIY COMMENTS FOR YOUR TEAM AND YOURSELF. YOU MAY NEED TO REVISIT CODE YOU WROTE OVER A YEAR AGO, AND IF YOU DONT COMMENT IT NOW YOU WONT REMEMBER WHY YOU DID WHAT YOU DID._\n"
      ],
      "id": "d976240c"
    },
    {
      "cell_type": "code",
      "metadata": {},
      "source": [
        "#| label: Q1\n",
        "#| code-summary: Read and format data\n",
        "# Include and execute your code here\n"
      ],
      "id": "Q1",
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "metadata": {},
      "source": [
        "## Question|Task 2\n",
        "\n",
        "__COPY PASTE QUESTION|TASK 2 FROM THE PROJECT HERE__\n",
        "\n",
        "- _include figures in chunks and discuss your findings in the figure._\n"
      ],
      "id": "0f4be015"
    },
    {
      "cell_type": "code",
      "metadata": {},
      "source": [
        "#| label: Q1-chart\n",
        "#| code-summary: plot example\n",
        "#| fig-cap: My useless chart\n",
        "#| fig-align: center\n",
        "# Include and execute your code here\n",
        "\n",
        "(\n",
        "  ggplot(df.head(500), aes(x='displ', y='hwy')) + geom_point()\n",
        ")"
      ],
      "id": "Q1-chart",
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "metadata": {},
      "source": [
        "## Question|Task 3\n",
        "\n",
        "__COPY PASTE QUESTION|TASK 3 FROM THE PROJECT HERE__\n",
        "\n",
        "- _PROVIDE TABLES THAT HELP ADDRESS THE QUESTIONS AND TASKS (IF APPLICABLE)._\n"
      ],
      "id": "97badc40"
    },
    {
      "cell_type": "code",
      "metadata": {},
      "source": [
        "#| label: Q1-table\n",
        "#| code-summary: table example\n",
        "#| tbl-cap: table example\n",
        "#| tbl-cap-location: top\n",
        "# Include and execute your code here\n",
        "mydat = (df.head(1000)\n",
        "    .groupby('manufacturer')\n",
        "    .sum()\n",
        "    .reset_index()\n",
        "    .tail(10)\n",
        "    .filter([\"manufacturer\",\"displ\",\"cty\", \"hwy\"])\n",
        ")\n",
        "\n",
        "display(mydat)"
      ],
      "id": "Q1-table",
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "metadata": {},
      "source": [
        "Note: Non executing Python `Snippets` include (3) \\`\\`\\` followed by (3) more \\`\\`\\`, each on their own line. These are not single quotes, they are the key left of the number 1 key on the keyboard. The top row can include the language of code that is pasted inbetween the \\`\\`\\`  marks. \n",
        "\n",
        "Note: These also work in `Slack` and it is expected they are used for any code shared in that app. No screen shots allowed."
      ],
      "id": "9c26e707"
    }
  ],
  "metadata": {
    "kernelspec": {
      "display_name": "Python 3",
      "language": "python",
      "name": "python3"
    }
  },
  "nbformat": 4,
  "nbformat_minor": 5
}