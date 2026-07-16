# Avance Semana 3 - COBRATRACK

## Proyecto

COBRATRACK - Sistema de Seguimiento y Control de Gestores de Cobranza en Campo mediante Geolocalización GPS.

## Actividades Realizadas

Durante la semana 3 se configuró el entorno de desarrollo colaborativo utilizando GitHub como plataforma de control de versiones.

Se creó la estructura inicial del proyecto mediante la organización de carpetas para documentación, pruebas, base de datos y código fuente.

## Módulo Desarrollado

Se implementó el módulo denominado **AcuerdoPago** ubicado en:

```text
src/core/acuerdo_pago.py
```

## Funcionalidad del Módulo

El módulo permite registrar acuerdos de pago realizados entre gestores de cobranza y clientes.

Las funciones implementadas son:

- Validación del identificador del cliente.
- Validación del monto del acuerdo.
- Validación de la fecha de compromiso.
- Determinación del estado del acuerdo.
- Generación de un resumen de la información registrada.

## Validaciones Implementadas

El sistema controla:

- Clientes con identificadores inválidos.
- Montos negativos o iguales a cero.
- Fechas vencidas o incorrectas.

## Pruebas

Se desarrolló el archivo:

```text
tests/test_acuerdo_pago.py
```

para verificar el correcto funcionamiento del módulo.

## Resultado

Se logró construir el primer componente funcional del proyecto COBRATRACK aplicando principios básicos de programación orientada a objetos y validaciones de negocio para garantizar la integridad de la información.
