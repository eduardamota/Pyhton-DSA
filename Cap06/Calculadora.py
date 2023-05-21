{
 "cells": [
  {
   "cell_type": "markdown",
   "id": "35707011",
   "metadata": {},
   "source": [
    "# Lab02\n",
    "Contrução de uma calculadora em Python, o que a calculadora deve ter:\n",
    "\n",
    "\n",
    "    Solicitar ao usuário que escolha a operação deseja;\n",
    "    Após escolher apresentar na tela quais números serão usados na operação."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "f7db1b25",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Selecione o número da operação desejada: \n",
      "\n",
      " 1- Soma \n",
      " 2- Subtração \n",
      " 3- Multiplicação \n",
      " 4 - divisão \n",
      "\n",
      "5\n",
      "Operação inválida!\n"
     ]
    }
   ],
   "source": [
    "tipo = float(input(\"Selecione o número da operação desejada: \\n\\n 1- Soma \\n 2- Subtração \\n 3- Multiplicação \\n 4 - divisão \\n\\n\" \n",
    "            ))\n",
    "if tipo == 1:\n",
    "    op1 = float(input(\"Digite sua primeira opção: \"))\n",
    "    op2 = float(input(\"Digite sua segunda opção: \"))\n",
    "    Resultado = op1 + op2 \n",
    "    print (\"O resultado é:\", Resultado)\n",
    "\n",
    "elif tipo == 2:\n",
    "    op1 = float(input(\"Digite sua primeira opção: \"))\n",
    "    op2 = float(input(\"Digite sua segunda opção: \"))\n",
    "    Resultado = op1 - op2 \n",
    "    print (\"O resultado é:\", Resultado)\n",
    "\n",
    "elif tipo == 3:\n",
    "    op1 = float(input(\"Digite sua primeira opção: \"))\n",
    "    op2 = float(input(\"Digite sua segunda opção: \"))\n",
    "    Resultado = op1 * op2 \n",
    "    print (\"O resultado é:\", Resultado)\n",
    "\n",
    "elif tipo == 4:\n",
    "    op1 = float(input(\"Digite sua primeira opção: \"))\n",
    "    op2 = float(input(\"Digite sua segunda opção: \"))\n",
    "    Resultado = op1 / op2 \n",
    "    print (\"O resultado é:\", Resultado)\n",
    "\n",
    "else:\n",
    "  print(\"Operação inválida!\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "89576b57",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.9.13"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
