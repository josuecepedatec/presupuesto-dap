from django.core.management.base import BaseCommand
from core.models import Area, SubArea, Proveedor, TipoDeGasto


AREAS = [
    'General',
    'Gerencia de Atracción de Posgrados',
    'Gerencia de Inteligencia de Negocios y Servicios para la Atracción',
    'Gerencia de Desarrollo y Efectividad Comercial de Educación Continua',
    'Gerencia de Atracción de Educación Continua',
    'Coordinación de Eficiencia Operativa',
    'DAP',
    'Gerencia de Inteligencia Comercial'
]

SUBAREAS = [
    'Inteligencia de Mercados',
    'Expansión y Despliegue de Oferta',
    'Generación de Demanda',
    'Inbound Marketing y Portales',
    'No_Aplica'
]

PROVEEDORES = [
    "XMARTICA",
    "Woorank",
    "Whitepaper (WP MEDIA S DE RL DE CV)",
    "UVETECH",
    "URBANSTARS SA DE CV",
    "Universidad Tecnológica Nacional – UTN.BA",
    "tyranosaurio",
    "Typeform S.L",
    "Twitter, Inc",
    "TOCA Creative Cluster S.A de C.V.",
    "TIKTOK MEXICO TECNOLOGIA",
    "The Software Optimization Focal Team, S. de R.L. de C.V.",
    "The Seven Seas Translations Agency, S.C.",
    "Tecnológico de Monterrey",
    "TCUX CONSULTORIA SC",
    "SV EVENTOS E INSTALACIONES SA DE CV",
    "Sputnik Digital, S.A.P.I. De C.V",
    "Smartup Mexico SA de CV",
    "Silvia Cervantes Contreras",
    "Shutterstock Inc",
    "Servicio de Comedores y Catering Tellez SA de CV",
    "Semrush Inc.",
    "Rosetta Stone",
    "Red Companies",
    "RECONOCIMIENTOS CREATIVOS, S.A. DE C.V.",
    "RECLA",
    "QUADRA PRODUCCIONES S DE RL DE CV",
    "Promo imagen",
    "Promo Bordados SA de CV",
    "PROKEEL S DE RL DE CV",
    "PLATZI SAPI DE CV",
    "Plato Express Operaciones S.A. de C.V.",
    "PARAMETROSTUDIO",
    "OPERADORA GASTRONOMICA LE GOURMET S CV",
    "OB-LISKO BANQUETES S.A DE C.V.",
    "Novemp (Edgar Martin Cano Ortiz)",
    "Mouseflow",
    "Mitzi Elizabeth Oliva Gleason",
    "MDY Servicios de Call Center",
    "Masterstudies AS",
    "Luis Ernesto Díaz García",
    "Lizbeth Perez Moreno",
    "LinkedIn",
    "Keystone Academic Solutions AS",
    "JUAN FRANCISCO ARIAS FLORES (VIDENS)",
    "Jose Guadalupe Rivera Luna",
    "Jessica de la Garza Cantu RFC: GACJ8308122U5",
    "Itzel Osuna Gutiérrez",
    "IPG MEDIA BRANDS COMMUNICATIONS SA DE CV",
    "INSPIRAL",
    "InboxLabs LLC",
    "IMM INTERNET MEDIA MEXICO",
    "IEBS Digital school",
    "ICNSA, SA DE CV",
    "HISPAVISTA MEXICO, S.A. DE C.V.",
    "Héctor Eder Carrera Flores",
    "GROU",
    "Google",
    "GoDaddy",
    "GELATTINA DE SABORES SA DE CV",
    "Gastos de Viaje",
    "formidableform",
    "Floreria San Borja",
    "Ferjo detalles",
    "Facebook",
    "Expo Posgradps",
    "ESTRATEGAS DE MARKETING DE MEXICO FUTURITE SA DE CV",
    "Erika Ruth Contreras Gelvez",
    "ERIAC Capital Humano AC",
    "Envia Flores",
    "Entreideas",
    "ENSITECH DE MEXICO SA DE CV",
    "EMAGISTER SERVICIOS DE FORMACIÓN S.L.",
    "EDUMARKET S DE RL DE CV",
    "EDUCAEDU BUSINESS, S.L.",
    "Ediciones el Norte SA de CV",
    "EDGAR MARTIN CANO ORTIZ",
    "Dulce sorpresa peru",
    "DTM Soluciones SC (Callpicker)",
    "Distribuidor de Experiencias Mexico S.A. de C.V.",
    "DIANA FABIOLA BELTRAN RODRIGUEZ",
    "DIALECT TELESERVICE SA DE CV",
    "Dettaglios",
    "Design Center / John Acuña",
    "Deliyum",
    "CYAN MEDIA LAB SA DE CV",
    "Consejo Mexicano de Estudios de Posgrado AC",
    "CONCENTRADORA DE MEDIOS PROMOCIONALES",
    "COMPAÑÍA MEXICANA DE INVERSIONES TURISTICAS SA DE CV",
    "CIBO NUTRIMENTAL SAPI DE CV",
    "Chocolates Clatt",
    "Carlos Americo Gonzalez Flores",
    "Canasta rosa",
    "BUENOS DIAS",
    "BETA PROMOCIONAL SA DE CV",
    "BERUMEN Y ASOCIADOS, SA DE CV",
    "BCD",
    "BARBARA BACKHOFF YUTANI",
    "B&S RESEARCH & CONSULTANCY SA DE CV",
    "Axtel",
    "Asociación Mexicana de Maestros de Ingles Mextesol A.C",
    "Artegraf",
    "ARKEEROMEX SAPI DE CV",
    "ARC Technology México",
    "Aprende más",
    "Angélica Carlos Devolder",
    "ANEXA",
    "Ana Velia de la Peña Peña",
    "AMEX-ITESM",
    "AMEDIRH",
    "Amazon",
    "ALLINKO CONSULTING",
    "Alestra",
    "AD FLAVOR, S.A DE C.V.",
    "AD FLAVOR, S.A DE C.V",
    "SERVICIOS DIGITALES EDUKAAP MEXICO S DE RL DE CV"
]

TIPOS_DE_GASTO = [
    'Capacit_formal_ext.',
    'Materiales_y_Equipos',
    'Publi_Prom_y_Propag',
    'Servicios',
    'Gastos_de_viaje'
]


class Command(BaseCommand):
    help = 'Carga datos iniciales en los modelos'

    def handle(self, *args, **kwargs):

        for nombre in AREAS:
            Area.objects.get_or_create(nombre=nombre)
            self.stdout.write(self.style.SUCCESS(f'Área "{nombre}" creada'))

        for nombre in SUBAREAS:
            SubArea.objects.get_or_create(nombre=nombre)
            self.stdout.write(self.style.SUCCESS(f'SubÁrea "{nombre}" creada'))

        for nombre in PROVEEDORES:
            Proveedor.objects.get_or_create(nombre=nombre)
            self.stdout.write(self.style.SUCCESS(f'Proveedor "{nombre}" creado'))

        for nombre in TIPOS_DE_GASTO:
            TipoDeGasto.objects.get_or_create(nombre=nombre)
            self.stdout.write(self.style.SUCCESS(f'Tipo de Gasto "{nombre}" creado'))

        self.stdout.write(self.style.SUCCESS('Datos iniciales cargados con éxito'))