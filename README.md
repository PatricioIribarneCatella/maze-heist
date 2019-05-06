# TDA - TP2

Resolución del [TP2 de la materia TDA de la FIUBA](https://algoritmos-rw.github.io/tda/2019-1c/tp2/)

### Run

#### Maze generator

```bash
 $ ./maze-generator.py METODO  LARGO  ANCHO
	
	METODO = ["dfs" | "dyc"]
	LARGO = entero positivo
	ANCHO = entero positivo
```

#### Maze solver

```bash
 $ ./maze-solver.py MAPA
	
	MAPA = "mapa-laberinto.txt" [default]
```

#### Maze plotter

```bash
 $ ./maze-plot.py TIPO-MAPA LABERINTO
	
	TIPO-MAPA = ["m" | "s"]
		- "m": mapa sin solucionar
		- "s": mapa con solución
	[Default]:
		LABERINTO = "mapa-laberinto.txt" (si TIPO-MAPA == "m")
		LABERINTO = "solucion-laberinto.txt" (si TIPO-MAPA == "s")
```

### Tests

```bash
 $ ./tester.sh
```

### Clean

```bash
 $ ./clean.sh
```

