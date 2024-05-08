import json

class Registro:
    def __init__(self, ficha_de_informaci_n_publicaci,
                 sexo,
                 peso,
                 talla_,
                 parto_atendido,
                 tiempo_gestaci_n_,
                 n_mero_consultas_prenatales,
                 tipo_parto,
                 mutiplicidad_,
                 apgar1,
                 apgar2,
                 grupo_sangu_neo_,
                 factor_rh,
                 pertenencia_tnica_,
                 estado_conyugal_madre,
                 nivel_educativo_,
                 pa_s_de_residencia_,
                 municipio_,
                 _rea_residencia_,
                 n_mero_hijos_nacidos_vivos_,
                 r_gimen_seguridad_,
                 nombre_administradora_,
                 nivel_educativo_padre):
        self.ficha_de_informaci_n_publicaci = ficha_de_informaci_n_publicaci
        self.sexo = sexo
        self.peso = float(peso)
        self.talla_ = float(talla_)
        self.parto_atendido = parto_atendido
        self.tiempo_gestaci_n_ = float(tiempo_gestaci_n_)
        self.n_mero_consultas_prenatales = n_mero_consultas_prenatales
        self.tipo_parto = tipo_parto
        self.mutiplicidad_ = mutiplicidad_
        self.apgar1 = apgar1
        self.apgar2 = apgar2
        self.grupo_sangu_neo_ = grupo_sangu_neo_
        self.factor_rh = factor_rh
        self.pertenencia_tnica_ = pertenencia_tnica_
        self.estado_conyugal_madre = estado_conyugal_madre
        self.nivel_educativo_ = nivel_educativo_
        self.pa_s_de_residencia_ = pa_s_de_residencia_
        self.municipio_ = municipio_
        self._rea_residencia_ = _rea_residencia_
        self.n_mero_hijos_nacidos_vivos_ = n_mero_hijos_nacidos_vivos_
        self.r_gimen_seguridad_ = r_gimen_seguridad_
        self.nombre_administradora_ = nombre_administradora_
        self.nivel_educativo_padre = nivel_educativo_padre

    def __str__(self):
        atributos = [
            f'ficha_de_informacion_publicacion: {self.ficha_de_informaci_n_publicaci}',
            f'sexo: {self.sexo}',
            f'peso: {self.peso}',
            f'talla: {self.talla_}',
            f'parto_atendido: {self.parto_atendido}',
            f'tiempo_gestacion: {self.tiempo_gestaci_n_}',
            f'n_mero_consultas_prenatales: {self.n_mero_consultas_prenatales}',
            f'tipo_parto: {self.tipo_parto}',
            f'mutiplicidad: {self.mutiplicidad_}',
            f'apgar1: {self.apgar1}',
            f'apgar2: {self.apgar2}',
            f'grupo_sanguineo: {self.grupo_sangu_neo_}',
            f'factor_rh: {self.factor_rh}',
            f'pertenencia_etnica: {self.pertenencia_tnica_}',
            f'estado_conyugal_madre: {self.estado_conyugal_madre}',
            f'nivel_educativo: {self.nivel_educativo_}',
            f'pais_de_residencia: {self.pa_s_de_residencia_}',
            f'municipio: {self.municipio_}',
            f'area_residencia: {self._rea_residencia_}',
            f'n_mero_hijos_nacidos_vivos: {self.n_mero_hijos_nacidos_vivos_}',
            f'regimen_seguridad: {self.r_gimen_seguridad_}',
            f'nombre_administradora: {self.nombre_administradora_}',
            f'nivel_educativo_padre: {self.nivel_educativo_padre}'
        ]
        return ", ".join(atributos)

    def printarray(array):
        for eo in array: print(eo)