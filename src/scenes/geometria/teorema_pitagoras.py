from manim import *

class ConstruccionCuadrados(Scene):

    # Definir los vértices del triángulo rectángulo
    A = np.array([-1.0, -0.7, 0.0])
    B = np.array([1.0, -0.7, 0.0])
    C = np.array([-1.0, 1.0, 0.0])

    def vertices(self):        
        A = self.A
        B = self.B
        C = self.C
        
        # Calcular los vectores de los catetos e hipotenusa
        cateto1 = B - A
        cateto2 = C - A
        hipotenusa = C - B
        
        ### Vertices
        self.Ac1 = A - rotate_vector(cateto1, PI/2)
        self.Bc1 = B - rotate_vector(cateto1, PI/2)
        self.Cc2 = C - rotate_vector(cateto2, -PI/2)
        self.Ac2 = A - rotate_vector(cateto2, -PI/2)
        self.Ch  = C - rotate_vector(hipotenusa, PI/2)
        self.Bh  = B - rotate_vector(hipotenusa, PI/2)
   
    def cuadrado_pitagoras(self,pt1,pt2,pt3,pt4,colorin,v1,v2):
        cuadrado = Polygon(pt1,pt2,pt3,pt4, color=colorin)
        self.play(Create(cuadrado))
        self.wait(1)
        self.etiqueta_1 = MathTex(v1).next_to(pt3, DOWN)
        self.etiqueta_2 = MathTex(v2).next_to(pt4, DOWN)
        self.play(Write(self.etiqueta_1),Write(self.etiqueta_2))
        return cuadrado
  
    def presentacion_inicial(self):
        titulo = Text("Demostración visual del Teorema de Pitágoras", font_size=36, color=BLUE)
        self.play(Write(titulo),run_time=2)
        self.wait(2)
        self.remove(titulo)

    
    def desplazamiento_total(self,arrays,grupo_grafico):
        # Definir una función para mover arrays
        def mover_arrays(arrays, desplazamiento):
            for i in range(len(arrays)):
                arrays[i] += desplazamiento[:3]

        # Mover el grupo gráfico hacia la izquierda
        desplazamiento = LEFT * 3  # Definir el desplazamiento
        grupo_grafico.shift(desplazamiento)

        # Mover los arrays usando la función
        mover_arrays(arrays, desplazamiento)

    def animar_texto(self, textos, tiempo_espera=1, tiempo_final=3):
        for texto in textos:
            self.play(Write(texto))
            self.wait(tiempo_espera)
        self.wait(tiempo_final)
        
    def demostracion(self,A,B,C,Bc1,Bh,Cc2,Ch,cuadrado1,cuadrado2,cuadrado3):
        linea1 = Line(C, Bc1, color=WHITE)
        linea2 = Line(A, Bh, color=YELLOW)
        linea3 = Line(B, Cc2, color=WHITE)
        linea4 = Line(A, Ch, color=YELLOW)
        
        #######
        self.play(Create(linea1),Create(linea2),run_time=5)
        etiqueta_cateto1 = MathTex("a").next_to(cuadrado1, UP)
        #self.play(Write(etiqueta_cateto1))
        #self.wait(1)
        # Crear las expresiones LaTeX
        texto_inicial = Tex("Del gráfico : \\\\Sea el cuadrado ABPQ de lado a")
        ecuacion1 = MathTex(r"S(\triangle PBC) = \frac{a^2}{2}")
        texto_intermedio0 = Tex("Por congruencia de triangulos:")
        ecuacion2 = MathTex(r"\triangle PBC \cong \triangle ABU")
        texto_intermedio = Tex("Entonces se tiene:")
        ecuacion3 = MathTex(r"S(\triangle ABU) = \frac{a^2}{2}")

        # Agrupar y posicionar en la esquina superior derecha
        grupo = VGroup(texto_inicial ,ecuacion1,texto_intermedio0, ecuacion2,texto_intermedio, ecuacion3).scale(0.75).arrange(DOWN, buff=0.5)
        grupo.to_edge(UP + RIGHT)

        textos = [texto_inicial,ecuacion1,texto_intermedio0,ecuacion2,texto_intermedio,ecuacion3]
        self.animar_texto(textos, tiempo_espera=1, tiempo_final=3)
        
        # Animar la desaparición de todas las expresiones
        self.play(FadeOut(grupo))
        self.wait(1)
        self.remove(linea1,linea2,etiqueta_cateto1)
        self.wait(1)

        ##########
        self.play(Create(linea3),Create(linea4),run_time=5)
        etiqueta_cateto2 = MathTex("b").next_to(cuadrado2, RIGHT)
        #self.play(Write(etiqueta_cateto2))
        #self.wait(1)
        # Crear las expresiones LaTeX
        texto_inicial = Tex("Como el lado del cuadrado ACRS es b , entonces:")
        ecuacion1 = MathTex(r"S(\triangle CRB) = \frac{b^2}{2}")
        texto_intermedio0 = Tex("Por congruencia de triangulos:")
        ecuacion2 = MathTex(r"\triangle CRB \cong \triangle ACT")
        texto_intermedio = Tex("Entonces se tiene:")
        ecuacion3 = MathTex(r"S(\triangle ACT) = \frac{b^2}{2}")

        # Agrupar y posicionar en la esquina superior derecha
        grupo = VGroup(texto_inicial ,ecuacion1,texto_intermedio0, ecuacion2, texto_intermedio ,ecuacion3).scale(0.75).arrange(DOWN, buff=0.5)
        grupo.to_edge(UP + RIGHT)

        textos = [texto_inicial,ecuacion1,texto_intermedio0,ecuacion2,texto_intermedio,ecuacion3]
        self.animar_texto(textos, tiempo_espera=1, tiempo_final=3)
        
        # Animar la desaparición de todas las expresiones
        self.play(FadeOut(grupo))
        self.wait(1)
        self.remove(linea3,linea4,etiqueta_cateto2)
        self.wait(1)

        ######
        self.play(Create(linea2),Create(linea4),run_time=5)
        etiqueta_hipotenusa = MathTex("c").next_to(cuadrado3, DOWN)
        #self.play(Write(etiqueta_hipotenusa))
        #self.wait(1)
        # Crear las expresiones LaTeX
        texto_inicial = Tex("Del gráfico y por teorema de areas:")
        ecuacion1 = MathTex(r"S(\triangle ABU)+S(\triangle ACT) = \frac{S(\square BCTU)}{2}")
        texto_intermedio0 = Tex("Como el lado del cuadrado es c :")
        ecuacion2 = MathTex(r"S(\square BCTU) = \frac{c^2}{2}")
        texto_intermedio = Tex("Entonces se tiene de las ecuaciones anteriores:")
        ecuacion3 = MathTex(r"\frac{a^2}{2}+\frac{b^2}{2} = \frac{c^2}{2}")
        ecuacion4 = MathTex(r"{a^2}+{b^2} = {c^2}")
        # Agrupar y posicionar en la esquina superior derecha
        grupo = VGroup(texto_inicial ,ecuacion1, texto_intermedio0,ecuacion2, texto_intermedio,ecuacion3,ecuacion4).scale(0.7).arrange(DOWN, buff=0.5)
        grupo.to_edge(UP + RIGHT)

        textos = [texto_inicial,ecuacion1,texto_intermedio0,ecuacion2,texto_intermedio,ecuacion3,ecuacion4]
        self.animar_texto(textos, tiempo_espera=1, tiempo_final=3)

        # Animar la desaparición de todas las expresiones
        self.play(FadeOut(grupo))
        self.wait(1)
        self.remove(linea2,linea4,etiqueta_hipotenusa)
        self.wait(1)
        
    def construct(self):

        ## Presentacion inicial
        self.presentacion_inicial()

        ## Asignacion de las coordenadas
        self.vertices()
        A   = self.A
        B   = self.B
        C   = self.C
        Ac1 = self.Ac1
        Ac2 = self.Ac2
        Bc1 = self.Bc1
        Bh  = self.Bh
        Cc2 = self.Cc2
        Ch  = self.Ch

        ## Creacion del triángulo principal y mostrar sus vertices
        triangulo = Polygon(A, B, C, color=WHITE)
        self.play(Create(triangulo))
        self.wait(1)

        etiqueta_A = MathTex("A").next_to(A, DOWN)
        etiqueta_B = MathTex("B").next_to(B, DOWN)
        etiqueta_C = MathTex("C").next_to(C, UP)
        self.play(Write(etiqueta_A),Write(etiqueta_B),Write(etiqueta_C))
    
        ## Mostrando los 3 cuadrados : cuadrado1 y cuadrado2 por los catetos
        ## y cuadrado3 por la hipotenusa
        cuadrado1=self.cuadrado_pitagoras(A,B,Bc1,Ac1,BLUE,"P","Q")
        etiqueta_Ac1 = self.etiqueta_1
        etiqueta_Bc1 = self.etiqueta_2

        cuadrado2=self.cuadrado_pitagoras(A,C,Cc2,Ac2,RED,"R","S")
        etiqueta_Cc2 = self.etiqueta_1
        etiqueta_Ac2 = self.etiqueta_2

        cuadrado3=self.cuadrado_pitagoras(B,C,Ch,Bh,GREEN,"T","U")
        etiqueta_Ch = self.etiqueta_1
        etiqueta_Bh = self.etiqueta_2

        ##Agrupando para el desplazamiento
        grupo_grafico = VGroup(
            triangulo, cuadrado1, cuadrado2, cuadrado3,
            etiqueta_A, etiqueta_Ac1, etiqueta_Ac2,
            etiqueta_B, etiqueta_Bc1, etiqueta_Bh,
            etiqueta_C, etiqueta_Cc2, etiqueta_Ch
        )
        # Lista de todos los arrays que necesitan ser movidos
        arrays = [A, B, C, Ac1, Bc1, Cc2, Ac2, Ch, Bh]

        #Desplazamiento de toda la figuras y arrays(A,B,C,...)
        self.desplazamiento_total(arrays,grupo_grafico)
        
        #Demostracion
        self.demostracion(A,B,C,Bc1,Bh,Cc2,Ch,cuadrado1,cuadrado2,cuadrado3)
        
        # Añadir etiquetas a los lados del triángulo
        etiqueta_cateto1 = MathTex("a").next_to(cuadrado1, UP)
        etiqueta_cateto2 = MathTex("b").next_to(cuadrado2, RIGHT)
        etiqueta_hipotenusa = MathTex("c").next_to(triangulo.get_center(), UP)
        self.play(Write(etiqueta_cateto1), Write(etiqueta_cateto2), Write(etiqueta_hipotenusa))
        self.wait(2)

        # Crear los textos
        texto_final = Tex("Teorema de Pitágoras: \\\\a² + b² = c²")
        texto_author = Tex("por Jose L.")

        # Agrupar los textos para posicionarlos juntos
        textos = VGroup(texto_final, texto_author)
        textos.arrange(DOWN, aligned_edge=RIGHT)  # Alinear al borde derecho y apilar verticalmente

        # Posicionar el grupo en el centro vertical, alineado a la derecha
        textos.to_edge(RIGHT)

        # Animar los textos
        self.play(Write(texto_final))
        self.play(Write(texto_author))
        self.wait(3)