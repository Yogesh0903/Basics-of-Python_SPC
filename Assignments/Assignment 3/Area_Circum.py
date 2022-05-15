{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "name": "Area_Circum.ipynb",
      "provenance": [],
      "authorship_tag": "ABX9TyNpR9KL+c2VF+L7TdAkHsdg"
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "l1zfDY9v9hQJ",
        "outputId": "2ecaa5eb-ad96-475f-bebb-86fbbffe0599"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            " The area of the given circle is:  7853.981633974483\n",
            " The circumference of the given circle is:  314.1592653589793\n"
          ]
        }
      ],
      "source": [
        "import math\n",
        "def Area_Circum(Radius):  \n",
        "  area = Radius** 2 * math.pi    \n",
        "  print (\" The area of the given circle is: \", area)\n",
        "  circumference = 2*math.pi*Radius\n",
        "  print (\" The circumference of the given circle is: \",circumference )\n",
        "Radius = 50 ### Given in the question\n",
        "Area_Circum(Radius) \n",
        "### Instead of Using math.pi we can also initializae pi as 3.14"
      ]
    }
  ]
}