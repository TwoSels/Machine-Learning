{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "name": "exercise1.ipynb",
      "provenance": [],
      "collapsed_sections": []
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
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "xMQ0F5mUyAgQ",
        "outputId": "233c9c61-b7f6-492f-acd1-45b4f8ba8a82"
      },
      "source": [
        "pip install panda"
      ],
      "execution_count": 21,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Requirement already satisfied: panda in /usr/local/lib/python3.7/dist-packages (0.3.1)\n",
            "Requirement already satisfied: setuptools in /usr/local/lib/python3.7/dist-packages (from panda) (57.4.0)\n",
            "Requirement already satisfied: requests in /usr/local/lib/python3.7/dist-packages (from panda) (2.23.0)\n",
            "Requirement already satisfied: chardet<4,>=3.0.2 in /usr/local/lib/python3.7/dist-packages (from requests->panda) (3.0.4)\n",
            "Requirement already satisfied: idna<3,>=2.5 in /usr/local/lib/python3.7/dist-packages (from requests->panda) (2.10)\n",
            "Requirement already satisfied: urllib3!=1.25.0,!=1.25.1,<1.26,>=1.21.1 in /usr/local/lib/python3.7/dist-packages (from requests->panda) (1.24.3)\n",
            "Requirement already satisfied: certifi>=2017.4.17 in /usr/local/lib/python3.7/dist-packages (from requests->panda) (2021.5.30)\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 315
        },
        "id": "fYo9bFWYyIfF",
        "outputId": "deb0450c-503f-4d94-b8b9-0e747062dca3"
      },
      "source": [
        "import pandas as pd\n",
        "# save filepath to variable for easier access\n",
        "melbourne_file_path = 'melb_data.csv'\n",
        "# read the data and store data in DataFrame titled melbourne_data\n",
        "melbourne_data = pd.read_csv(melbourne_file_path) \n",
        "# print a summary of the data in Melbourne data\n",
        "melbourne_data.describe()"
      ],
      "execution_count": 22,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/html": [
              "<div>\n",
              "<style scoped>\n",
              "    .dataframe tbody tr th:only-of-type {\n",
              "        vertical-align: middle;\n",
              "    }\n",
              "\n",
              "    .dataframe tbody tr th {\n",
              "        vertical-align: top;\n",
              "    }\n",
              "\n",
              "    .dataframe thead th {\n",
              "        text-align: right;\n",
              "    }\n",
              "</style>\n",
              "<table border=\"1\" class=\"dataframe\">\n",
              "  <thead>\n",
              "    <tr style=\"text-align: right;\">\n",
              "      <th></th>\n",
              "      <th>Rooms</th>\n",
              "      <th>Price</th>\n",
              "      <th>Distance</th>\n",
              "      <th>Postcode</th>\n",
              "      <th>Bedroom2</th>\n",
              "      <th>Bathroom</th>\n",
              "      <th>Car</th>\n",
              "      <th>Landsize</th>\n",
              "      <th>BuildingArea</th>\n",
              "      <th>YearBuilt</th>\n",
              "      <th>Lattitude</th>\n",
              "      <th>Longtitude</th>\n",
              "      <th>Propertycount</th>\n",
              "    </tr>\n",
              "  </thead>\n",
              "  <tbody>\n",
              "    <tr>\n",
              "      <th>count</th>\n",
              "      <td>13580.000000</td>\n",
              "      <td>1.358000e+04</td>\n",
              "      <td>13580.000000</td>\n",
              "      <td>13580.000000</td>\n",
              "      <td>13580.000000</td>\n",
              "      <td>13580.000000</td>\n",
              "      <td>13518.000000</td>\n",
              "      <td>13580.000000</td>\n",
              "      <td>7130.000000</td>\n",
              "      <td>8205.000000</td>\n",
              "      <td>13580.000000</td>\n",
              "      <td>13580.000000</td>\n",
              "      <td>13580.000000</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>mean</th>\n",
              "      <td>2.937997</td>\n",
              "      <td>1.075684e+06</td>\n",
              "      <td>10.137776</td>\n",
              "      <td>3105.301915</td>\n",
              "      <td>2.914728</td>\n",
              "      <td>1.534242</td>\n",
              "      <td>1.610075</td>\n",
              "      <td>558.416127</td>\n",
              "      <td>151.967650</td>\n",
              "      <td>1964.684217</td>\n",
              "      <td>-37.809203</td>\n",
              "      <td>144.995216</td>\n",
              "      <td>7454.417378</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>std</th>\n",
              "      <td>0.955748</td>\n",
              "      <td>6.393107e+05</td>\n",
              "      <td>5.868725</td>\n",
              "      <td>90.676964</td>\n",
              "      <td>0.965921</td>\n",
              "      <td>0.691712</td>\n",
              "      <td>0.962634</td>\n",
              "      <td>3990.669241</td>\n",
              "      <td>541.014538</td>\n",
              "      <td>37.273762</td>\n",
              "      <td>0.079260</td>\n",
              "      <td>0.103916</td>\n",
              "      <td>4378.581772</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>min</th>\n",
              "      <td>1.000000</td>\n",
              "      <td>8.500000e+04</td>\n",
              "      <td>0.000000</td>\n",
              "      <td>3000.000000</td>\n",
              "      <td>0.000000</td>\n",
              "      <td>0.000000</td>\n",
              "      <td>0.000000</td>\n",
              "      <td>0.000000</td>\n",
              "      <td>0.000000</td>\n",
              "      <td>1196.000000</td>\n",
              "      <td>-38.182550</td>\n",
              "      <td>144.431810</td>\n",
              "      <td>249.000000</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>25%</th>\n",
              "      <td>2.000000</td>\n",
              "      <td>6.500000e+05</td>\n",
              "      <td>6.100000</td>\n",
              "      <td>3044.000000</td>\n",
              "      <td>2.000000</td>\n",
              "      <td>1.000000</td>\n",
              "      <td>1.000000</td>\n",
              "      <td>177.000000</td>\n",
              "      <td>93.000000</td>\n",
              "      <td>1940.000000</td>\n",
              "      <td>-37.856822</td>\n",
              "      <td>144.929600</td>\n",
              "      <td>4380.000000</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>50%</th>\n",
              "      <td>3.000000</td>\n",
              "      <td>9.030000e+05</td>\n",
              "      <td>9.200000</td>\n",
              "      <td>3084.000000</td>\n",
              "      <td>3.000000</td>\n",
              "      <td>1.000000</td>\n",
              "      <td>2.000000</td>\n",
              "      <td>440.000000</td>\n",
              "      <td>126.000000</td>\n",
              "      <td>1970.000000</td>\n",
              "      <td>-37.802355</td>\n",
              "      <td>145.000100</td>\n",
              "      <td>6555.000000</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>75%</th>\n",
              "      <td>3.000000</td>\n",
              "      <td>1.330000e+06</td>\n",
              "      <td>13.000000</td>\n",
              "      <td>3148.000000</td>\n",
              "      <td>3.000000</td>\n",
              "      <td>2.000000</td>\n",
              "      <td>2.000000</td>\n",
              "      <td>651.000000</td>\n",
              "      <td>174.000000</td>\n",
              "      <td>1999.000000</td>\n",
              "      <td>-37.756400</td>\n",
              "      <td>145.058305</td>\n",
              "      <td>10331.000000</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>max</th>\n",
              "      <td>10.000000</td>\n",
              "      <td>9.000000e+06</td>\n",
              "      <td>48.100000</td>\n",
              "      <td>3977.000000</td>\n",
              "      <td>20.000000</td>\n",
              "      <td>8.000000</td>\n",
              "      <td>10.000000</td>\n",
              "      <td>433014.000000</td>\n",
              "      <td>44515.000000</td>\n",
              "      <td>2018.000000</td>\n",
              "      <td>-37.408530</td>\n",
              "      <td>145.526350</td>\n",
              "      <td>21650.000000</td>\n",
              "    </tr>\n",
              "  </tbody>\n",
              "</table>\n",
              "</div>"
            ],
            "text/plain": [
              "              Rooms         Price  ...    Longtitude  Propertycount\n",
              "count  13580.000000  1.358000e+04  ...  13580.000000   13580.000000\n",
              "mean       2.937997  1.075684e+06  ...    144.995216    7454.417378\n",
              "std        0.955748  6.393107e+05  ...      0.103916    4378.581772\n",
              "min        1.000000  8.500000e+04  ...    144.431810     249.000000\n",
              "25%        2.000000  6.500000e+05  ...    144.929600    4380.000000\n",
              "50%        3.000000  9.030000e+05  ...    145.000100    6555.000000\n",
              "75%        3.000000  1.330000e+06  ...    145.058305   10331.000000\n",
              "max       10.000000  9.000000e+06  ...    145.526350   21650.000000\n",
              "\n",
              "[8 rows x 13 columns]"
            ]
          },
          "metadata": {},
          "execution_count": 22
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "6IWlbjxTySq_",
        "outputId": "29e44f1e-bf4d-47ca-cf16-9c9dd6e09d30"
      },
      "source": [
        "melbourne_data.columns"
      ],
      "execution_count": 23,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "Index(['Suburb', 'Address', 'Rooms', 'Type', 'Price', 'Method', 'SellerG',\n",
              "       'Date', 'Distance', 'Postcode', 'Bedroom2', 'Bathroom', 'Car',\n",
              "       'Landsize', 'BuildingArea', 'YearBuilt', 'CouncilArea', 'Lattitude',\n",
              "       'Longtitude', 'Regionname', 'Propertycount'],\n",
              "      dtype='object')"
            ]
          },
          "metadata": {},
          "execution_count": 23
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "jLvmo_AdyYbP"
      },
      "source": [
        "# The Melbourne data has some missing values (some houses for which some variables weren't recorded.)\n",
        "# We'll learn to handle missing values in a later tutorial.  \n",
        "# Your Iowa data doesn't have missing values in the columns you use. \n",
        "# So we will take the simplest option for now, and drop houses from our data. \n",
        "# Don't worry about this much for now, though the code is:\n",
        "\n",
        "# dropna drops missing values (think of na as \"not available\")\n",
        "melbourne_data = melbourne_data.dropna(axis=0)"
      ],
      "execution_count": 24,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "eGygMUkbyiwN"
      },
      "source": [
        "y = melbourne_data.Price"
      ],
      "execution_count": 25,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "_v7ngsN2ykFM"
      },
      "source": [
        "melbourne_features = ['Rooms', 'Bathroom', 'Landsize', 'Lattitude', 'Longtitude']"
      ],
      "execution_count": 26,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "L98AXWkzypDM"
      },
      "source": [
        "X = melbourne_data[melbourne_features]"
      ],
      "execution_count": 27,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 295
        },
        "id": "nF0wS-9Qywqz",
        "outputId": "3d4fb7b9-3942-434c-f8dd-2a8708bfba73"
      },
      "source": [
        "X.describe()"
      ],
      "execution_count": 28,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/html": [
              "<div>\n",
              "<style scoped>\n",
              "    .dataframe tbody tr th:only-of-type {\n",
              "        vertical-align: middle;\n",
              "    }\n",
              "\n",
              "    .dataframe tbody tr th {\n",
              "        vertical-align: top;\n",
              "    }\n",
              "\n",
              "    .dataframe thead th {\n",
              "        text-align: right;\n",
              "    }\n",
              "</style>\n",
              "<table border=\"1\" class=\"dataframe\">\n",
              "  <thead>\n",
              "    <tr style=\"text-align: right;\">\n",
              "      <th></th>\n",
              "      <th>Rooms</th>\n",
              "      <th>Bathroom</th>\n",
              "      <th>Landsize</th>\n",
              "      <th>Lattitude</th>\n",
              "      <th>Longtitude</th>\n",
              "    </tr>\n",
              "  </thead>\n",
              "  <tbody>\n",
              "    <tr>\n",
              "      <th>count</th>\n",
              "      <td>6196.000000</td>\n",
              "      <td>6196.000000</td>\n",
              "      <td>6196.000000</td>\n",
              "      <td>6196.000000</td>\n",
              "      <td>6196.000000</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>mean</th>\n",
              "      <td>2.931407</td>\n",
              "      <td>1.576340</td>\n",
              "      <td>471.006940</td>\n",
              "      <td>-37.807904</td>\n",
              "      <td>144.990201</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>std</th>\n",
              "      <td>0.971079</td>\n",
              "      <td>0.711362</td>\n",
              "      <td>897.449881</td>\n",
              "      <td>0.075850</td>\n",
              "      <td>0.099165</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>min</th>\n",
              "      <td>1.000000</td>\n",
              "      <td>1.000000</td>\n",
              "      <td>0.000000</td>\n",
              "      <td>-38.164920</td>\n",
              "      <td>144.542370</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>25%</th>\n",
              "      <td>2.000000</td>\n",
              "      <td>1.000000</td>\n",
              "      <td>152.000000</td>\n",
              "      <td>-37.855438</td>\n",
              "      <td>144.926198</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>50%</th>\n",
              "      <td>3.000000</td>\n",
              "      <td>1.000000</td>\n",
              "      <td>373.000000</td>\n",
              "      <td>-37.802250</td>\n",
              "      <td>144.995800</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>75%</th>\n",
              "      <td>4.000000</td>\n",
              "      <td>2.000000</td>\n",
              "      <td>628.000000</td>\n",
              "      <td>-37.758200</td>\n",
              "      <td>145.052700</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>max</th>\n",
              "      <td>8.000000</td>\n",
              "      <td>8.000000</td>\n",
              "      <td>37000.000000</td>\n",
              "      <td>-37.457090</td>\n",
              "      <td>145.526350</td>\n",
              "    </tr>\n",
              "  </tbody>\n",
              "</table>\n",
              "</div>"
            ],
            "text/plain": [
              "             Rooms     Bathroom      Landsize    Lattitude   Longtitude\n",
              "count  6196.000000  6196.000000   6196.000000  6196.000000  6196.000000\n",
              "mean      2.931407     1.576340    471.006940   -37.807904   144.990201\n",
              "std       0.971079     0.711362    897.449881     0.075850     0.099165\n",
              "min       1.000000     1.000000      0.000000   -38.164920   144.542370\n",
              "25%       2.000000     1.000000    152.000000   -37.855438   144.926198\n",
              "50%       3.000000     1.000000    373.000000   -37.802250   144.995800\n",
              "75%       4.000000     2.000000    628.000000   -37.758200   145.052700\n",
              "max       8.000000     8.000000  37000.000000   -37.457090   145.526350"
            ]
          },
          "metadata": {},
          "execution_count": 28
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 203
        },
        "id": "dw8BPMD6y2Rv",
        "outputId": "48b0924c-6331-420c-f3fb-83cd33b06913"
      },
      "source": [
        "X.head()"
      ],
      "execution_count": 29,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/html": [
              "<div>\n",
              "<style scoped>\n",
              "    .dataframe tbody tr th:only-of-type {\n",
              "        vertical-align: middle;\n",
              "    }\n",
              "\n",
              "    .dataframe tbody tr th {\n",
              "        vertical-align: top;\n",
              "    }\n",
              "\n",
              "    .dataframe thead th {\n",
              "        text-align: right;\n",
              "    }\n",
              "</style>\n",
              "<table border=\"1\" class=\"dataframe\">\n",
              "  <thead>\n",
              "    <tr style=\"text-align: right;\">\n",
              "      <th></th>\n",
              "      <th>Rooms</th>\n",
              "      <th>Bathroom</th>\n",
              "      <th>Landsize</th>\n",
              "      <th>Lattitude</th>\n",
              "      <th>Longtitude</th>\n",
              "    </tr>\n",
              "  </thead>\n",
              "  <tbody>\n",
              "    <tr>\n",
              "      <th>1</th>\n",
              "      <td>2</td>\n",
              "      <td>1.0</td>\n",
              "      <td>156.0</td>\n",
              "      <td>-37.8079</td>\n",
              "      <td>144.9934</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>2</th>\n",
              "      <td>3</td>\n",
              "      <td>2.0</td>\n",
              "      <td>134.0</td>\n",
              "      <td>-37.8093</td>\n",
              "      <td>144.9944</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>4</th>\n",
              "      <td>4</td>\n",
              "      <td>1.0</td>\n",
              "      <td>120.0</td>\n",
              "      <td>-37.8072</td>\n",
              "      <td>144.9941</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>6</th>\n",
              "      <td>3</td>\n",
              "      <td>2.0</td>\n",
              "      <td>245.0</td>\n",
              "      <td>-37.8024</td>\n",
              "      <td>144.9993</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>7</th>\n",
              "      <td>2</td>\n",
              "      <td>1.0</td>\n",
              "      <td>256.0</td>\n",
              "      <td>-37.8060</td>\n",
              "      <td>144.9954</td>\n",
              "    </tr>\n",
              "  </tbody>\n",
              "</table>\n",
              "</div>"
            ],
            "text/plain": [
              "   Rooms  Bathroom  Landsize  Lattitude  Longtitude\n",
              "1      2       1.0     156.0   -37.8079    144.9934\n",
              "2      3       2.0     134.0   -37.8093    144.9944\n",
              "4      4       1.0     120.0   -37.8072    144.9941\n",
              "6      3       2.0     245.0   -37.8024    144.9993\n",
              "7      2       1.0     256.0   -37.8060    144.9954"
            ]
          },
          "metadata": {},
          "execution_count": 29
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "UxjdnX7Dy72u",
        "outputId": "9eac7126-6575-445b-8bf0-9263b5a7984a"
      },
      "source": [
        "from sklearn.tree import DecisionTreeRegressor\n",
        "\n",
        "# Define model. Specify a number for random_state to ensure same results each run\n",
        "melbourne_model = DecisionTreeRegressor(random_state=1)\n",
        "\n",
        "# Fit model\n",
        "melbourne_model.fit(X, y)"
      ],
      "execution_count": 30,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "DecisionTreeRegressor(ccp_alpha=0.0, criterion='mse', max_depth=None,\n",
              "                      max_features=None, max_leaf_nodes=None,\n",
              "                      min_impurity_decrease=0.0, min_impurity_split=None,\n",
              "                      min_samples_leaf=1, min_samples_split=2,\n",
              "                      min_weight_fraction_leaf=0.0, presort='deprecated',\n",
              "                      random_state=1, splitter='best')"
            ]
          },
          "metadata": {},
          "execution_count": 30
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "4_D0t8cWzBXb",
        "outputId": "7b18b82a-d6cc-49ed-8f29-0fb652d58a86"
      },
      "source": [
        "print(\"Making predictions for the following 5 houses:\")\n",
        "print(X.head())\n",
        "print(\"The predictions are\")\n",
        "print(melbourne_model.predict(X.head()))"
      ],
      "execution_count": 31,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Making predictions for the following 5 houses:\n",
            "   Rooms  Bathroom  Landsize  Lattitude  Longtitude\n",
            "1      2       1.0     156.0   -37.8079    144.9934\n",
            "2      3       2.0     134.0   -37.8093    144.9944\n",
            "4      4       1.0     120.0   -37.8072    144.9941\n",
            "6      3       2.0     245.0   -37.8024    144.9993\n",
            "7      2       1.0     256.0   -37.8060    144.9954\n",
            "The predictions are\n",
            "[1035000. 1465000. 1600000. 1876000. 1636000.]\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "WYoTV8Z_zP_f",
        "outputId": "231a213b-72ec-4d98-c774-97f776cd46b7"
      },
      "source": [
        "# Data Loading Code Hidden Here\n",
        "import pandas as pd\n",
        " \n",
        "# Filter rows with missing price values\n",
        "filtered_melbourne_data = melbourne_data.dropna(axis=0)\n",
        "# Choose target and features\n",
        "y = filtered_melbourne_data.Price\n",
        "melbourne_features = ['Rooms', 'Bathroom', 'Landsize', 'BuildingArea', \n",
        "                        'YearBuilt', 'Lattitude', 'Longtitude']\n",
        "X = filtered_melbourne_data[melbourne_features]\n",
        "\n",
        "from sklearn.tree import DecisionTreeRegressor\n",
        "# Define model\n",
        "melbourne_model = DecisionTreeRegressor()\n",
        "# Fit model\n",
        "melbourne_model.fit(X, y)"
      ],
      "execution_count": 32,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "DecisionTreeRegressor(ccp_alpha=0.0, criterion='mse', max_depth=None,\n",
              "                      max_features=None, max_leaf_nodes=None,\n",
              "                      min_impurity_decrease=0.0, min_impurity_split=None,\n",
              "                      min_samples_leaf=1, min_samples_split=2,\n",
              "                      min_weight_fraction_leaf=0.0, presort='deprecated',\n",
              "                      random_state=None, splitter='best')"
            ]
          },
          "metadata": {},
          "execution_count": 32
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "XNP0FDb2zWWh",
        "outputId": "95f73c75-f4e2-48ea-c1d9-fc2736ca6f32"
      },
      "source": [
        "from sklearn.metrics import mean_absolute_error\n",
        "\n",
        "predicted_home_prices = melbourne_model.predict(X)\n",
        "mean_absolute_error(y, predicted_home_prices)"
      ],
      "execution_count": 33,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "434.71594577146544"
            ]
          },
          "metadata": {},
          "execution_count": 33
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "ta1wbSESzcaY",
        "outputId": "1c84e9c4-9c03-4974-c86e-6350e6e67ff9"
      },
      "source": [
        "from sklearn.model_selection import train_test_split\n",
        "\n",
        "# split data into training and validation data, for both features and target\n",
        "# The split is based on a random number generator. Supplying a numeric value to\n",
        "# the random_state argument guarantees we get the same split every time we\n",
        "# run this script.\n",
        "train_X, val_X, train_y, val_y = train_test_split(X, y, random_state = 0)\n",
        "# Define model\n",
        "melbourne_model = DecisionTreeRegressor()\n",
        "# Fit model\n",
        "melbourne_model.fit(train_X, train_y)\n",
        "\n",
        "# get predicted prices on validation data\n",
        "val_predictions = melbourne_model.predict(val_X)\n",
        "print(mean_absolute_error(val_y, val_predictions))"
      ],
      "execution_count": 34,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "262090.00193673337\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "NuWkZbgyzhY9"
      },
      "source": [
        "from sklearn.metrics import mean_absolute_error\n",
        "from sklearn.tree import DecisionTreeRegressor\n",
        "\n",
        "def get_mae(max_leaf_nodes, train_X, val_X, train_y, val_y):\n",
        "    model = DecisionTreeRegressor(max_leaf_nodes=max_leaf_nodes, random_state=0)\n",
        "    model.fit(train_X, train_y)\n",
        "    preds_val = model.predict(val_X)\n",
        "    mae = mean_absolute_error(val_y, preds_val)\n",
        "    return(mae)"
      ],
      "execution_count": 35,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "9Xm2oxUhzinL"
      },
      "source": [
        "# Data Loading Code Runs At This Point\n",
        "import pandas as pd\n",
        "    \n",
        "# Filter rows with missing values\n",
        "filtered_melbourne_data = melbourne_data.dropna(axis=0)\n",
        "# Choose target and features\n",
        "y = filtered_melbourne_data.Price\n",
        "melbourne_features = ['Rooms', 'Bathroom', 'Landsize', 'BuildingArea', \n",
        "                        'YearBuilt', 'Lattitude', 'Longtitude']\n",
        "X = filtered_melbourne_data[melbourne_features]\n",
        "\n",
        "from sklearn.model_selection import train_test_split\n",
        "\n",
        "# split data into training and validation data, for both features and target\n",
        "train_X, val_X, train_y, val_y = train_test_split(X, y,random_state = 0)"
      ],
      "execution_count": 36,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "qbzOyFgazpNB",
        "outputId": "b32214a6-ce15-4429-bb75-d1fc5a77ac0e"
      },
      "source": [
        "# compare MAE with differing values of max_leaf_nodes\n",
        "for max_leaf_nodes in [5, 50, 500, 5000]:\n",
        "    my_mae = get_mae(max_leaf_nodes, train_X, val_X, train_y, val_y)\n",
        "    print(\"Max leaf nodes: %d  \\t\\t Mean Absolute Error:  %d\" %(max_leaf_nodes, my_mae))"
      ],
      "execution_count": 37,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Max leaf nodes: 5  \t\t Mean Absolute Error:  347380\n",
            "Max leaf nodes: 50  \t\t Mean Absolute Error:  258171\n",
            "Max leaf nodes: 500  \t\t Mean Absolute Error:  243495\n",
            "Max leaf nodes: 5000  \t\t Mean Absolute Error:  254983\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "f0W63g25zuQU"
      },
      "source": [
        "import pandas as pd\n",
        "    \n",
        "# Filter rows with missing values\n",
        "melbourne_data = melbourne_data.dropna(axis=0)\n",
        "# Choose target and features\n",
        "y = melbourne_data.Price\n",
        "melbourne_features = ['Rooms', 'Bathroom', 'Landsize', 'BuildingArea', \n",
        "                        'YearBuilt', 'Lattitude', 'Longtitude']\n",
        "X = melbourne_data[melbourne_features]\n",
        "\n",
        "from sklearn.model_selection import train_test_split\n",
        "\n",
        "# split data into training and validation data, for both features and target\n",
        "# The split is based on a random number generator. Supplying a numeric value to\n",
        "# the random_state argument guarantees we get the same split every time we\n",
        "# run this script.\n",
        "train_X, val_X, train_y, val_y = train_test_split(X, y,random_state = 0)"
      ],
      "execution_count": 38,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "dvyXNwoazy0r",
        "outputId": "ab77d961-76dc-472d-ef84-de5d21299085"
      },
      "source": [
        "from sklearn.ensemble import RandomForestRegressor\n",
        "from sklearn.metrics import mean_absolute_error\n",
        "\n",
        "forest_model = RandomForestRegressor(random_state=1)\n",
        "forest_model.fit(train_X, train_y)\n",
        "melb_preds = forest_model.predict(val_X)\n",
        "print(mean_absolute_error(val_y, melb_preds))"
      ],
      "execution_count": 39,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "191669.7536453626\n"
          ]
        }
      ]
    }
  ]
}
