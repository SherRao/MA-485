from distutils.cygwinccompiler import CONFIG_H_UNCERTAIN
from pygame import Color, Vector3;

LEFT_MOUSE_BUTTON = 1;

# The masses of the planets in the solar system, measured in kg.
M_mercury = 3.3022e23;
M_venus = 4.8685e24;
M_earth = 5.9736e24;
M_moon = 7.3477e22;
M_mars = 6.4185e23;
M_jupiter = 1.8986e27;
M_saturn = 5.6846e26;
M_uranus = 8.6810e25;
M_neptune = 1.0243e26;
M_pluto = 1.312e22;

# Initial positions for the planets in the solar system, measured in m.
P_sun = Vector3(0, 0, 0);
P_mercury = Vector3(5.791e10, 0, 0);
P_venus = Vector3(1.0821e11, 0, 0);
P_earth = Vector3(1.496e11, 0, 0);
P_moon = Vector3(1.496e11 + 3.844e8, 0, 0);
P_mars = Vector3(2.2794e11, 0, 0);
P_jupiter = Vector3(7.7857e11, 0, 0);
P_saturn = Vector3(1.4335e12, 0, 0);
P_uranus = Vector3(2.8725e12, 0, 0);
P_neptune = Vector3(4.4951e12, 0, 0);
P_pluto = Vector3(5.9064e12, 0, 0);

# Initial velocities for the planets in the solar system, measured in m/s.
V_sun = Vector3(0, 0, 0);
V_mercury = Vector3(0, 4.787e4, 0);
V_venus = Vector3(0, 3.502e4, 0);
V_earth = Vector3(0, 2.978e4, 0);
V_moon = Vector3(0, 2.978e4 + 1.022e3, 0);
V_mars = Vector3(0, 2.4077e4, 0);
V_jupiter = Vector3(0, 1.307e4, 0);
V_saturn = Vector3(0, 9.69e3, 0);
V_uranus = Vector3(0, 6.81e3, 0);
V_neptune = Vector3(0, 5.43e3, 0);
V_pluto = Vector3(0, 4.67e3, 0);

# The colors of the planets in the solar system.
C_sun = Color(253, 184, 19);
C_mercury = Color(184, 184, 184);
C_venus = Color(200, 200, 200);
C_earth = Color(40, 122, 184);
C_moon = Color(200, 200, 200);
C_mars = Color(184, 40, 40);
C_jupiter = Color(156, 63, 48);
C_saturn = Color(184, 156, 48);
C_uranus = Color(48, 156, 184);
C_neptune = Color(48, 63, 156);
C_pluto = Color(156, 48, 63);
