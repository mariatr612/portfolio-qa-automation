Feature: Login en Spotify

  Como usuario de Spotify
  Quiero poder iniciar sesión con mis credenciales
  Para acceder a mi cuenta y reproducir música

  Scenario Outline: Inicio de sesión exitoso
    Given que el usuario está en la página de login de Spotify
    When ingresa su email <user> y contraseña <password>
    And presiona el botón de iniciar sesión
 #  Then debería ver la página de inicio de Spotify

     Examples:
  | user                   | password          |
  | "mariatr612@gmail.com" | "Sp3032Sp..."     |

 # Scenario Outline: Inicio de sesión fallido con contraseña incorrecta
#  Given que el usuario está en la página de login de Spotify
 #  When ingresa su email <user> y contraseña <password>
# And presiona el botón de iniciar sesión
#  Then debería ver un mensaje de error "Usuario o contraseña incorrectos"

#Scenario Outline: Inicio de sesión fallido con email inválido
#   Given que el usuario está en la página de login de Spotify
#   When ingresa su email <user> y contraseña <password>
#  And presiona el botón de iniciar sesión
#   Then debería ver un mensaje de error "Introduce un email válido"

#   Examples:
#| user                   | password          |
# | "mariatr612@gmail.com" | "Sp3032Sp..."     |