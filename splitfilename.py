{
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/yun2590/Exercise_2025/blob/main/splitfilename.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "def splitFilename(file):\n",
        "  buf=file.split('.')\n",
        "  if len(buf)>1:\n",
        "    ext=buf[-1]\n",
        "    fname='.'.join(buf[:-1])\n",
        "  else:\n",
        "    fname=buf[0]\n",
        "    ext=None\n",
        "  return (fname,ext)"
      ],
      "metadata": {
        "id": "zO2Vo6V44rnD"
      },
      "execution_count": 50,
      "outputs": []
    }
  ],
  "metadata": {
    "colab": {
      "name": "Colab 시작하기",
      "provenance": [],
      "include_colab_link": true
    },
    "kernelspec": {
      "display_name": "Python 3",
      "name": "python3"
    }
  },
  "nbformat": 4,
  "nbformat_minor": 0
}