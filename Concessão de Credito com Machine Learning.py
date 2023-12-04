{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "name": "Concessão de Crédito com Machine Learning.ipynb",
      "provenance": [],
      "toc_visible": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "pG-o99QvFlS4"
      },
      "source": [
        "# Configurações"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "aiXgHWzaKgcO"
      },
      "source": [
        "![alt text](https://github.com/elthonf/plataformas-cognitivas-docker/blob/master/images/capa.png?raw=1)"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "AII-AcywAFml"
      },
      "source": [
        "#@title Parâmetros da solução\n",
        "#@markdown Informe a quantidade de clientes que devem ser analisados.\n",
        "qtde_clientes = 4  #@param {type: \"slider\", min: 1, max: 10}\n",
        "\n",
        "#@markdown Informe o IP do servidor de predição da sua solução:\n",
        "my_server_ip = \"20.169.140.158\" #@param {type:\"string\"}\n",
        "\n",
        "#@markdown Informe a porta do servidor de predição da sua solução, se nada foi alterado, deve ser 443:\n",
        "my_server_port = \"443\" #@param {type:\"string\"}\n",
        "\n",
        "#@markdown Informe o seu nome:\n",
        "students_name = \"Claudio Santos\" #@param {type:\"string\"}\n",
        "\n",
        "#@markdown Ah, e não se esqueça de executar esta célula!\n"
      ],
      "execution_count": 26,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "bL7_Uitf-_Uv"
      },
      "source": [
        "import requests\n",
        "import pandas as pd\n",
        "import json"
      ],
      "execution_count": 27,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "EnnjKg0_-6Q4"
      },
      "source": [
        "# Obtenção dos empréstimos pendentes de análise\n",
        "\n",
        "Vamos agora obter os clientes que estã precisand de empréstimo e exibí-los na tela"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "HO5QEWjz_eYk"
      },
      "source": [
        "url = \"https://us-central1-emf-teacher.cloudfunctions.net/function-aulas-getclient?qtde={0}\".format(qtde_clientes)\n",
        "headers = {'Content-Type': 'application/json'}\n",
        "response = requests.request(\"GET\", url, headers=headers)\n",
        "response_content = response.text.encode('utf8').decode()\n",
        "clientes = pd.read_json(response_content)"
      ],
      "execution_count": 28,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "Yg6oYQyw_sXc",
        "outputId": "dd963119-1d35-4623-ba7a-ffae8afc0cd2",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 175
        }
      },
      "source": [
        "clientes"
      ],
      "execution_count": 29,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "                   nome        renda      idade  etnia  sexo  casapropria  \\\n",
              "33906      Erin, Bucher  4798.007409  42.022393      0     1            1   \n",
              "47544   Ryan, Vangelder  2137.044002  49.575217      1     0            1   \n",
              "16314    Rasheed, Hardy  2169.222738  22.358875      1     0            1   \n",
              "279    Ziyaad, al-Emami  4594.717201  25.798339      0     0            1   \n",
              "\n",
              "       outrasrendas  estadocivil  escolaridade  \n",
              "33906             0            1             3  \n",
              "47544             0            0             2  \n",
              "16314             0            0             1  \n",
              "279               0            1             1  "
            ],
            "text/html": [
              "\n",
              "  <div id=\"df-bbf8cb0e-877a-46b6-8f49-bb954ce9f9be\" class=\"colab-df-container\">\n",
              "    <div>\n",
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
              "      <th>nome</th>\n",
              "      <th>renda</th>\n",
              "      <th>idade</th>\n",
              "      <th>etnia</th>\n",
              "      <th>sexo</th>\n",
              "      <th>casapropria</th>\n",
              "      <th>outrasrendas</th>\n",
              "      <th>estadocivil</th>\n",
              "      <th>escolaridade</th>\n",
              "    </tr>\n",
              "  </thead>\n",
              "  <tbody>\n",
              "    <tr>\n",
              "      <th>33906</th>\n",
              "      <td>Erin, Bucher</td>\n",
              "      <td>4798.007409</td>\n",
              "      <td>42.022393</td>\n",
              "      <td>0</td>\n",
              "      <td>1</td>\n",
              "      <td>1</td>\n",
              "      <td>0</td>\n",
              "      <td>1</td>\n",
              "      <td>3</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>47544</th>\n",
              "      <td>Ryan, Vangelder</td>\n",
              "      <td>2137.044002</td>\n",
              "      <td>49.575217</td>\n",
              "      <td>1</td>\n",
              "      <td>0</td>\n",
              "      <td>1</td>\n",
              "      <td>0</td>\n",
              "      <td>0</td>\n",
              "      <td>2</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>16314</th>\n",
              "      <td>Rasheed, Hardy</td>\n",
              "      <td>2169.222738</td>\n",
              "      <td>22.358875</td>\n",
              "      <td>1</td>\n",
              "      <td>0</td>\n",
              "      <td>1</td>\n",
              "      <td>0</td>\n",
              "      <td>0</td>\n",
              "      <td>1</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>279</th>\n",
              "      <td>Ziyaad, al-Emami</td>\n",
              "      <td>4594.717201</td>\n",
              "      <td>25.798339</td>\n",
              "      <td>0</td>\n",
              "      <td>0</td>\n",
              "      <td>1</td>\n",
              "      <td>0</td>\n",
              "      <td>1</td>\n",
              "      <td>1</td>\n",
              "    </tr>\n",
              "  </tbody>\n",
              "</table>\n",
              "</div>\n",
              "    <div class=\"colab-df-buttons\">\n",
              "\n",
              "  <div class=\"colab-df-container\">\n",
              "    <button class=\"colab-df-convert\" onclick=\"convertToInteractive('df-bbf8cb0e-877a-46b6-8f49-bb954ce9f9be')\"\n",
              "            title=\"Convert this dataframe to an interactive table.\"\n",
              "            style=\"display:none;\">\n",
              "\n",
              "  <svg xmlns=\"http://www.w3.org/2000/svg\" height=\"24px\" viewBox=\"0 -960 960 960\">\n",
              "    <path d=\"M120-120v-720h720v720H120Zm60-500h600v-160H180v160Zm220 220h160v-160H400v160Zm0 220h160v-160H400v160ZM180-400h160v-160H180v160Zm440 0h160v-160H620v160ZM180-180h160v-160H180v160Zm440 0h160v-160H620v160Z\"/>\n",
              "  </svg>\n",
              "    </button>\n",
              "\n",
              "  <style>\n",
              "    .colab-df-container {\n",
              "      display:flex;\n",
              "      gap: 12px;\n",
              "    }\n",
              "\n",
              "    .colab-df-convert {\n",
              "      background-color: #E8F0FE;\n",
              "      border: none;\n",
              "      border-radius: 50%;\n",
              "      cursor: pointer;\n",
              "      display: none;\n",
              "      fill: #1967D2;\n",
              "      height: 32px;\n",
              "      padding: 0 0 0 0;\n",
              "      width: 32px;\n",
              "    }\n",
              "\n",
              "    .colab-df-convert:hover {\n",
              "      background-color: #E2EBFA;\n",
              "      box-shadow: 0px 1px 2px rgba(60, 64, 67, 0.3), 0px 1px 3px 1px rgba(60, 64, 67, 0.15);\n",
              "      fill: #174EA6;\n",
              "    }\n",
              "\n",
              "    .colab-df-buttons div {\n",
              "      margin-bottom: 4px;\n",
              "    }\n",
              "\n",
              "    [theme=dark] .colab-df-convert {\n",
              "      background-color: #3B4455;\n",
              "      fill: #D2E3FC;\n",
              "    }\n",
              "\n",
              "    [theme=dark] .colab-df-convert:hover {\n",
              "      background-color: #434B5C;\n",
              "      box-shadow: 0px 1px 3px 1px rgba(0, 0, 0, 0.15);\n",
              "      filter: drop-shadow(0px 1px 2px rgba(0, 0, 0, 0.3));\n",
              "      fill: #FFFFFF;\n",
              "    }\n",
              "  </style>\n",
              "\n",
              "    <script>\n",
              "      const buttonEl =\n",
              "        document.querySelector('#df-bbf8cb0e-877a-46b6-8f49-bb954ce9f9be button.colab-df-convert');\n",
              "      buttonEl.style.display =\n",
              "        google.colab.kernel.accessAllowed ? 'block' : 'none';\n",
              "\n",
              "      async function convertToInteractive(key) {\n",
              "        const element = document.querySelector('#df-bbf8cb0e-877a-46b6-8f49-bb954ce9f9be');\n",
              "        const dataTable =\n",
              "          await google.colab.kernel.invokeFunction('convertToInteractive',\n",
              "                                                    [key], {});\n",
              "        if (!dataTable) return;\n",
              "\n",
              "        const docLinkHtml = 'Like what you see? Visit the ' +\n",
              "          '<a target=\"_blank\" href=https://colab.research.google.com/notebooks/data_table.ipynb>data table notebook</a>'\n",
              "          + ' to learn more about interactive tables.';\n",
              "        element.innerHTML = '';\n",
              "        dataTable['output_type'] = 'display_data';\n",
              "        await google.colab.output.renderOutput(dataTable, element);\n",
              "        const docLink = document.createElement('div');\n",
              "        docLink.innerHTML = docLinkHtml;\n",
              "        element.appendChild(docLink);\n",
              "      }\n",
              "    </script>\n",
              "  </div>\n",
              "\n",
              "\n",
              "<div id=\"df-e6266519-20c3-4486-bc16-a5510b51580a\">\n",
              "  <button class=\"colab-df-quickchart\" onclick=\"quickchart('df-e6266519-20c3-4486-bc16-a5510b51580a')\"\n",
              "            title=\"Suggest charts\"\n",
              "            style=\"display:none;\">\n",
              "\n",
              "<svg xmlns=\"http://www.w3.org/2000/svg\" height=\"24px\"viewBox=\"0 0 24 24\"\n",
              "     width=\"24px\">\n",
              "    <g>\n",
              "        <path d=\"M19 3H5c-1.1 0-2 .9-2 2v14c0 1.1.9 2 2 2h14c1.1 0 2-.9 2-2V5c0-1.1-.9-2-2-2zM9 17H7v-7h2v7zm4 0h-2V7h2v10zm4 0h-2v-4h2v4z\"/>\n",
              "    </g>\n",
              "</svg>\n",
              "  </button>\n",
              "\n",
              "<style>\n",
              "  .colab-df-quickchart {\n",
              "      --bg-color: #E8F0FE;\n",
              "      --fill-color: #1967D2;\n",
              "      --hover-bg-color: #E2EBFA;\n",
              "      --hover-fill-color: #174EA6;\n",
              "      --disabled-fill-color: #AAA;\n",
              "      --disabled-bg-color: #DDD;\n",
              "  }\n",
              "\n",
              "  [theme=dark] .colab-df-quickchart {\n",
              "      --bg-color: #3B4455;\n",
              "      --fill-color: #D2E3FC;\n",
              "      --hover-bg-color: #434B5C;\n",
              "      --hover-fill-color: #FFFFFF;\n",
              "      --disabled-bg-color: #3B4455;\n",
              "      --disabled-fill-color: #666;\n",
              "  }\n",
              "\n",
              "  .colab-df-quickchart {\n",
              "    background-color: var(--bg-color);\n",
              "    border: none;\n",
              "    border-radius: 50%;\n",
              "    cursor: pointer;\n",
              "    display: none;\n",
              "    fill: var(--fill-color);\n",
              "    height: 32px;\n",
              "    padding: 0;\n",
              "    width: 32px;\n",
              "  }\n",
              "\n",
              "  .colab-df-quickchart:hover {\n",
              "    background-color: var(--hover-bg-color);\n",
              "    box-shadow: 0 1px 2px rgba(60, 64, 67, 0.3), 0 1px 3px 1px rgba(60, 64, 67, 0.15);\n",
              "    fill: var(--button-hover-fill-color);\n",
              "  }\n",
              "\n",
              "  .colab-df-quickchart-complete:disabled,\n",
              "  .colab-df-quickchart-complete:disabled:hover {\n",
              "    background-color: var(--disabled-bg-color);\n",
              "    fill: var(--disabled-fill-color);\n",
              "    box-shadow: none;\n",
              "  }\n",
              "\n",
              "  .colab-df-spinner {\n",
              "    border: 2px solid var(--fill-color);\n",
              "    border-color: transparent;\n",
              "    border-bottom-color: var(--fill-color);\n",
              "    animation:\n",
              "      spin 1s steps(1) infinite;\n",
              "  }\n",
              "\n",
              "  @keyframes spin {\n",
              "    0% {\n",
              "      border-color: transparent;\n",
              "      border-bottom-color: var(--fill-color);\n",
              "      border-left-color: var(--fill-color);\n",
              "    }\n",
              "    20% {\n",
              "      border-color: transparent;\n",
              "      border-left-color: var(--fill-color);\n",
              "      border-top-color: var(--fill-color);\n",
              "    }\n",
              "    30% {\n",
              "      border-color: transparent;\n",
              "      border-left-color: var(--fill-color);\n",
              "      border-top-color: var(--fill-color);\n",
              "      border-right-color: var(--fill-color);\n",
              "    }\n",
              "    40% {\n",
              "      border-color: transparent;\n",
              "      border-right-color: var(--fill-color);\n",
              "      border-top-color: var(--fill-color);\n",
              "    }\n",
              "    60% {\n",
              "      border-color: transparent;\n",
              "      border-right-color: var(--fill-color);\n",
              "    }\n",
              "    80% {\n",
              "      border-color: transparent;\n",
              "      border-right-color: var(--fill-color);\n",
              "      border-bottom-color: var(--fill-color);\n",
              "    }\n",
              "    90% {\n",
              "      border-color: transparent;\n",
              "      border-bottom-color: var(--fill-color);\n",
              "    }\n",
              "  }\n",
              "</style>\n",
              "\n",
              "  <script>\n",
              "    async function quickchart(key) {\n",
              "      const quickchartButtonEl =\n",
              "        document.querySelector('#' + key + ' button');\n",
              "      quickchartButtonEl.disabled = true;  // To prevent multiple clicks.\n",
              "      quickchartButtonEl.classList.add('colab-df-spinner');\n",
              "      try {\n",
              "        const charts = await google.colab.kernel.invokeFunction(\n",
              "            'suggestCharts', [key], {});\n",
              "      } catch (error) {\n",
              "        console.error('Error during call to suggestCharts:', error);\n",
              "      }\n",
              "      quickchartButtonEl.classList.remove('colab-df-spinner');\n",
              "      quickchartButtonEl.classList.add('colab-df-quickchart-complete');\n",
              "    }\n",
              "    (() => {\n",
              "      let quickchartButtonEl =\n",
              "        document.querySelector('#df-e6266519-20c3-4486-bc16-a5510b51580a button');\n",
              "      quickchartButtonEl.style.display =\n",
              "        google.colab.kernel.accessAllowed ? 'block' : 'none';\n",
              "    })();\n",
              "  </script>\n",
              "</div>\n",
              "    </div>\n",
              "  </div>\n"
            ]
          },
          "metadata": {},
          "execution_count": 29
        }
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "I8VIiDB8GaLw"
      },
      "source": [
        "# Predição\n",
        "\n",
        "O cliente agora será submetido a dois modelos de Machine Learning preparados para a análise."
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "qE27sOO0GPFC"
      },
      "source": [
        "url = \"http://{}:{}/predict\".format(my_server_ip, my_server_port)\n",
        "headers = {'Content-Type': 'application/json'}\n",
        "conteudo = clientes.to_json()"
      ],
      "execution_count": 30,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "print(conteudo)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "MdoeAYfHvFSJ",
        "outputId": "ae92a1f9-4b3d-4ad5-888a-958fbc692ad8"
      },
      "execution_count": 38,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "{\"nome\":{\"33906\":\"Erin, Bucher\",\"47544\":\"Ryan, Vangelder\",\"16314\":\"Rasheed, Hardy\",\"279\":\"Ziyaad, al-Emami\"},\"renda\":{\"33906\":4798.0074094827,\"47544\":2137.0440024022,\"16314\":2169.2227380703,\"279\":4594.7172007624},\"idade\":{\"33906\":42.0223934735,\"47544\":49.5752167361,\"16314\":22.3588745739,\"279\":25.7983391868},\"etnia\":{\"33906\":0,\"47544\":1,\"16314\":1,\"279\":0},\"sexo\":{\"33906\":1,\"47544\":0,\"16314\":0,\"279\":0},\"casapropria\":{\"33906\":1,\"47544\":1,\"16314\":1,\"279\":1},\"outrasrendas\":{\"33906\":0,\"47544\":0,\"16314\":0,\"279\":0},\"estadocivil\":{\"33906\":1,\"47544\":0,\"16314\":0,\"279\":1},\"escolaridade\":{\"33906\":3,\"47544\":2,\"16314\":1,\"279\":1}}\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "print(url)"
      ],
      "metadata": {
        "id": "FIi3KiCKtR_H",
        "outputId": "cec5abef-e0b4-40b0-8dc7-239a135081d8",
        "colab": {
          "base_uri": "https://localhost:8080/"
        }
      },
      "execution_count": 32,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "http://20.169.140.158:443/predict\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "ufspC1N0ExsM",
        "outputId": "dbd9c0fa-b5c4-4a75-fa55-fc75671c5d92",
        "colab": {
          "base_uri": "https://localhost:8080/"
        }
      },
      "source": [
        "response01 = requests.request(\"POST\", url + f\"?model=modelo01&aluno=Claudio Santos\", headers=headers, data=conteudo)\n",
        "respostas01 = json.loads(response01.text.encode('utf8').decode())\n",
        "respostas01"
      ],
      "execution_count": 33,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "{'prediction': [0, 1, 1, 0],\n",
              " 'proba': [[0.9990064378714653, 0.0009935621285347578],\n",
              "  [0.000777841742396923, 0.9992221582576031],\n",
              "  [0.00046520353650569835, 0.9995347964634943],\n",
              "  [0.9963147817932859, 0.00368521820671412]]}"
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
        "id": "S_O_UBleE05F"
      },
      "source": [
        "df_01 = pd.Series(respostas01['prediction'], index = clientes.index, name=\"PredicaoML01\")\n",
        "df_01B = pd.Series(respostas01['proba'], index = clientes.index, name=\"PredicaoML01B\")"
      ],
      "execution_count": 34,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "3X_p_bAPFXhr",
        "outputId": "8ce1ea43-e040-44ca-e9c4-166c6e0409a2",
        "colab": {
          "base_uri": "https://localhost:8080/"
        }
      },
      "source": [
        "response02 = requests.request(\"POST\", url + \"?model=modelo02\", headers=headers, data=conteudo)\n",
        "respostas02 = json.loads(response02.text.encode('utf8').decode())\n",
        "respostas02"
      ],
      "execution_count": 35,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "{'prediction': [-0.0002760512672581496,\n",
              "  1.0011924703942845,\n",
              "  1.0353475448623755,\n",
              "  0.037180087745211136]}"
            ]
          },
          "metadata": {},
          "execution_count": 35
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "A10MTY8tG_8d"
      },
      "source": [
        "df_02 = pd.Series(respostas02['prediction'], index = clientes.index, name=\"PredicaoML02\")"
      ],
      "execution_count": 36,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "KrVb0COfE2p6",
        "outputId": "c925f736-eb48-44a1-f6c4-63c538ffc1df",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 175
        }
      },
      "source": [
        "pd.DataFrame(clientes.loc[:,\"nome\"])\\\n",
        "    .merge(right= df_01, left_index=True, right_index=True)\\\n",
        "    .merge(df_01B, left_index=True, right_index=True)\\\n",
        "    .merge(df_02, left_index=True, right_index=True)"
      ],
      "execution_count": 37,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "                   nome  PredicaoML01  \\\n",
              "33906      Erin, Bucher             0   \n",
              "47544   Ryan, Vangelder             1   \n",
              "16314    Rasheed, Hardy             1   \n",
              "279    Ziyaad, al-Emami             0   \n",
              "\n",
              "                                      PredicaoML01B  PredicaoML02  \n",
              "33906   [0.9990064378714653, 0.0009935621285347578]     -0.000276  \n",
              "47544    [0.000777841742396923, 0.9992221582576031]      1.001192  \n",
              "16314  [0.00046520353650569835, 0.9995347964634943]      1.035348  \n",
              "279       [0.9963147817932859, 0.00368521820671412]      0.037180  "
            ],
            "text/html": [
              "\n",
              "  <div id=\"df-5f23bada-e579-4e73-8e9c-6e05b6275125\" class=\"colab-df-container\">\n",
              "    <div>\n",
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
              "      <th>nome</th>\n",
              "      <th>PredicaoML01</th>\n",
              "      <th>PredicaoML01B</th>\n",
              "      <th>PredicaoML02</th>\n",
              "    </tr>\n",
              "  </thead>\n",
              "  <tbody>\n",
              "    <tr>\n",
              "      <th>33906</th>\n",
              "      <td>Erin, Bucher</td>\n",
              "      <td>0</td>\n",
              "      <td>[0.9990064378714653, 0.0009935621285347578]</td>\n",
              "      <td>-0.000276</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>47544</th>\n",
              "      <td>Ryan, Vangelder</td>\n",
              "      <td>1</td>\n",
              "      <td>[0.000777841742396923, 0.9992221582576031]</td>\n",
              "      <td>1.001192</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>16314</th>\n",
              "      <td>Rasheed, Hardy</td>\n",
              "      <td>1</td>\n",
              "      <td>[0.00046520353650569835, 0.9995347964634943]</td>\n",
              "      <td>1.035348</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>279</th>\n",
              "      <td>Ziyaad, al-Emami</td>\n",
              "      <td>0</td>\n",
              "      <td>[0.9963147817932859, 0.00368521820671412]</td>\n",
              "      <td>0.037180</td>\n",
              "    </tr>\n",
              "  </tbody>\n",
              "</table>\n",
              "</div>\n",
              "    <div class=\"colab-df-buttons\">\n",
              "\n",
              "  <div class=\"colab-df-container\">\n",
              "    <button class=\"colab-df-convert\" onclick=\"convertToInteractive('df-5f23bada-e579-4e73-8e9c-6e05b6275125')\"\n",
              "            title=\"Convert this dataframe to an interactive table.\"\n",
              "            style=\"display:none;\">\n",
              "\n",
              "  <svg xmlns=\"http://www.w3.org/2000/svg\" height=\"24px\" viewBox=\"0 -960 960 960\">\n",
              "    <path d=\"M120-120v-720h720v720H120Zm60-500h600v-160H180v160Zm220 220h160v-160H400v160Zm0 220h160v-160H400v160ZM180-400h160v-160H180v160Zm440 0h160v-160H620v160ZM180-180h160v-160H180v160Zm440 0h160v-160H620v160Z\"/>\n",
              "  </svg>\n",
              "    </button>\n",
              "\n",
              "  <style>\n",
              "    .colab-df-container {\n",
              "      display:flex;\n",
              "      gap: 12px;\n",
              "    }\n",
              "\n",
              "    .colab-df-convert {\n",
              "      background-color: #E8F0FE;\n",
              "      border: none;\n",
              "      border-radius: 50%;\n",
              "      cursor: pointer;\n",
              "      display: none;\n",
              "      fill: #1967D2;\n",
              "      height: 32px;\n",
              "      padding: 0 0 0 0;\n",
              "      width: 32px;\n",
              "    }\n",
              "\n",
              "    .colab-df-convert:hover {\n",
              "      background-color: #E2EBFA;\n",
              "      box-shadow: 0px 1px 2px rgba(60, 64, 67, 0.3), 0px 1px 3px 1px rgba(60, 64, 67, 0.15);\n",
              "      fill: #174EA6;\n",
              "    }\n",
              "\n",
              "    .colab-df-buttons div {\n",
              "      margin-bottom: 4px;\n",
              "    }\n",
              "\n",
              "    [theme=dark] .colab-df-convert {\n",
              "      background-color: #3B4455;\n",
              "      fill: #D2E3FC;\n",
              "    }\n",
              "\n",
              "    [theme=dark] .colab-df-convert:hover {\n",
              "      background-color: #434B5C;\n",
              "      box-shadow: 0px 1px 3px 1px rgba(0, 0, 0, 0.15);\n",
              "      filter: drop-shadow(0px 1px 2px rgba(0, 0, 0, 0.3));\n",
              "      fill: #FFFFFF;\n",
              "    }\n",
              "  </style>\n",
              "\n",
              "    <script>\n",
              "      const buttonEl =\n",
              "        document.querySelector('#df-5f23bada-e579-4e73-8e9c-6e05b6275125 button.colab-df-convert');\n",
              "      buttonEl.style.display =\n",
              "        google.colab.kernel.accessAllowed ? 'block' : 'none';\n",
              "\n",
              "      async function convertToInteractive(key) {\n",
              "        const element = document.querySelector('#df-5f23bada-e579-4e73-8e9c-6e05b6275125');\n",
              "        const dataTable =\n",
              "          await google.colab.kernel.invokeFunction('convertToInteractive',\n",
              "                                                    [key], {});\n",
              "        if (!dataTable) return;\n",
              "\n",
              "        const docLinkHtml = 'Like what you see? Visit the ' +\n",
              "          '<a target=\"_blank\" href=https://colab.research.google.com/notebooks/data_table.ipynb>data table notebook</a>'\n",
              "          + ' to learn more about interactive tables.';\n",
              "        element.innerHTML = '';\n",
              "        dataTable['output_type'] = 'display_data';\n",
              "        await google.colab.output.renderOutput(dataTable, element);\n",
              "        const docLink = document.createElement('div');\n",
              "        docLink.innerHTML = docLinkHtml;\n",
              "        element.appendChild(docLink);\n",
              "      }\n",
              "    </script>\n",
              "  </div>\n",
              "\n",
              "\n",
              "<div id=\"df-c50c660e-e08f-4c88-84cd-f89509cdc540\">\n",
              "  <button class=\"colab-df-quickchart\" onclick=\"quickchart('df-c50c660e-e08f-4c88-84cd-f89509cdc540')\"\n",
              "            title=\"Suggest charts\"\n",
              "            style=\"display:none;\">\n",
              "\n",
              "<svg xmlns=\"http://www.w3.org/2000/svg\" height=\"24px\"viewBox=\"0 0 24 24\"\n",
              "     width=\"24px\">\n",
              "    <g>\n",
              "        <path d=\"M19 3H5c-1.1 0-2 .9-2 2v14c0 1.1.9 2 2 2h14c1.1 0 2-.9 2-2V5c0-1.1-.9-2-2-2zM9 17H7v-7h2v7zm4 0h-2V7h2v10zm4 0h-2v-4h2v4z\"/>\n",
              "    </g>\n",
              "</svg>\n",
              "  </button>\n",
              "\n",
              "<style>\n",
              "  .colab-df-quickchart {\n",
              "      --bg-color: #E8F0FE;\n",
              "      --fill-color: #1967D2;\n",
              "      --hover-bg-color: #E2EBFA;\n",
              "      --hover-fill-color: #174EA6;\n",
              "      --disabled-fill-color: #AAA;\n",
              "      --disabled-bg-color: #DDD;\n",
              "  }\n",
              "\n",
              "  [theme=dark] .colab-df-quickchart {\n",
              "      --bg-color: #3B4455;\n",
              "      --fill-color: #D2E3FC;\n",
              "      --hover-bg-color: #434B5C;\n",
              "      --hover-fill-color: #FFFFFF;\n",
              "      --disabled-bg-color: #3B4455;\n",
              "      --disabled-fill-color: #666;\n",
              "  }\n",
              "\n",
              "  .colab-df-quickchart {\n",
              "    background-color: var(--bg-color);\n",
              "    border: none;\n",
              "    border-radius: 50%;\n",
              "    cursor: pointer;\n",
              "    display: none;\n",
              "    fill: var(--fill-color);\n",
              "    height: 32px;\n",
              "    padding: 0;\n",
              "    width: 32px;\n",
              "  }\n",
              "\n",
              "  .colab-df-quickchart:hover {\n",
              "    background-color: var(--hover-bg-color);\n",
              "    box-shadow: 0 1px 2px rgba(60, 64, 67, 0.3), 0 1px 3px 1px rgba(60, 64, 67, 0.15);\n",
              "    fill: var(--button-hover-fill-color);\n",
              "  }\n",
              "\n",
              "  .colab-df-quickchart-complete:disabled,\n",
              "  .colab-df-quickchart-complete:disabled:hover {\n",
              "    background-color: var(--disabled-bg-color);\n",
              "    fill: var(--disabled-fill-color);\n",
              "    box-shadow: none;\n",
              "  }\n",
              "\n",
              "  .colab-df-spinner {\n",
              "    border: 2px solid var(--fill-color);\n",
              "    border-color: transparent;\n",
              "    border-bottom-color: var(--fill-color);\n",
              "    animation:\n",
              "      spin 1s steps(1) infinite;\n",
              "  }\n",
              "\n",
              "  @keyframes spin {\n",
              "    0% {\n",
              "      border-color: transparent;\n",
              "      border-bottom-color: var(--fill-color);\n",
              "      border-left-color: var(--fill-color);\n",
              "    }\n",
              "    20% {\n",
              "      border-color: transparent;\n",
              "      border-left-color: var(--fill-color);\n",
              "      border-top-color: var(--fill-color);\n",
              "    }\n",
              "    30% {\n",
              "      border-color: transparent;\n",
              "      border-left-color: var(--fill-color);\n",
              "      border-top-color: var(--fill-color);\n",
              "      border-right-color: var(--fill-color);\n",
              "    }\n",
              "    40% {\n",
              "      border-color: transparent;\n",
              "      border-right-color: var(--fill-color);\n",
              "      border-top-color: var(--fill-color);\n",
              "    }\n",
              "    60% {\n",
              "      border-color: transparent;\n",
              "      border-right-color: var(--fill-color);\n",
              "    }\n",
              "    80% {\n",
              "      border-color: transparent;\n",
              "      border-right-color: var(--fill-color);\n",
              "      border-bottom-color: var(--fill-color);\n",
              "    }\n",
              "    90% {\n",
              "      border-color: transparent;\n",
              "      border-bottom-color: var(--fill-color);\n",
              "    }\n",
              "  }\n",
              "</style>\n",
              "\n",
              "  <script>\n",
              "    async function quickchart(key) {\n",
              "      const quickchartButtonEl =\n",
              "        document.querySelector('#' + key + ' button');\n",
              "      quickchartButtonEl.disabled = true;  // To prevent multiple clicks.\n",
              "      quickchartButtonEl.classList.add('colab-df-spinner');\n",
              "      try {\n",
              "        const charts = await google.colab.kernel.invokeFunction(\n",
              "            'suggestCharts', [key], {});\n",
              "      } catch (error) {\n",
              "        console.error('Error during call to suggestCharts:', error);\n",
              "      }\n",
              "      quickchartButtonEl.classList.remove('colab-df-spinner');\n",
              "      quickchartButtonEl.classList.add('colab-df-quickchart-complete');\n",
              "    }\n",
              "    (() => {\n",
              "      let quickchartButtonEl =\n",
              "        document.querySelector('#df-c50c660e-e08f-4c88-84cd-f89509cdc540 button');\n",
              "      quickchartButtonEl.style.display =\n",
              "        google.colab.kernel.accessAllowed ? 'block' : 'none';\n",
              "    })();\n",
              "  </script>\n",
              "</div>\n",
              "    </div>\n",
              "  </div>\n"
            ]
          },
          "metadata": {},
          "execution_count": 37
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "xoppo_YQE-mt"
      },
      "source": [],
      "execution_count": null,
      "outputs": []
    }
  ]
}