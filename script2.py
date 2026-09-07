import turtle
import random
import math

# ==========================================
# CONSTANTS & SCREEN ARCHITECTURE
# ==========================================
WIDTH, HEIGHT = 1000, 750
screen = turtle.Screen()
screen.setup(width=WIDTH, height=HEIGHT)
screen.bgcolor("#020208")  # Ultra deep space void blue
screen.title("Python Cosmic Simulation Engine Pro: Earth Orbit Edition")
screen.tracer(0)  # Enables micro-managed screen buffer updates

# Dynamic stack tracking visual particle states
explosions = []


# ==========================================
# CELESTIAL GRAPHICS OBJECTS (OOP CLASSES)
# ==========================================

class Sun:
    """Manages a stationary glowing sun at the core center of the system."""

    def __init__(self, x, y, radius):
        self.x = x
        self.y = y
        self.radius = radius

    def draw(self, t):
        # Layered ring distribution to simulate a dynamic atmospheric aura
        for i in range(12, 0, -1):
            r = (self.radius / 12) * i
            t.penup()
            t.goto(self.x, self.y - r)
            t.pendown()
            t.color("#FF4500" if i > 8 else "#FFA500" if i > 4 else "#FFFF00")
            t.begin_fill()
            t.circle(r)
            t.end_fill()


class OrbitingPlanet:
    """Calculates continuous circular trajectories around an orbital focal point."""

    def __init__(self, center_x, center_y, orbit_radius, radius, color, speed, name=""):
        self.center_x = center_x
        self.center_y = center_y
        self.orbit_radius = orbit_radius
        self.radius = radius
        self.color = color
        self.speed = speed
        self.name = name
        self.angle = random.uniform(0, 2 * math.pi)  # Balanced distributed start angle
        self.x = 0
        self.y = 0
        self.moon_angle = 0

    def update(self):
        # Advance the position angle along the primary orbit path
        self.angle += self.speed

        # Apply standard coordinate geometry transformations
        self.x = self.center_x + math.cos(self.angle) * self.orbit_radius
        self.y = self.center_y + math.sin(self.angle) * self.orbit_radius

        # Advance satellite rotational positioning
        self.moon_angle += 0.06

    def draw(self, t):
        # Draw clean, faint orbital ring paths
        t.penup()
        t.goto(self.center_x, self.center_y - self.orbit_radius)
        t.pendown()
        t.color("#111122")
        t.pensize(1)
        t.circle(self.orbit_radius)

        # Draw primary planetary mass
        t.penup()
        t.goto(self.x, self.y - self.radius)
        t.pendown()
        t.color(self.color)
        t.begin_fill()
        t.circle(self.radius)
        t.end_fill()

        # Add continent details if the object is explicitly Earth
        if self.name == "Earth":
            t.penup()
            t.goto(self.x + 2, self.y)
            t.pendown()
            t.dot(self.radius, "#228B22")  # Forest green landmass simulation

        # Draw moon orbiting the planet mass locally
        moon_x = self.x + math.cos(self.moon_angle) * (self.radius * 2.2)
        moon_y = self.y + math.sin(self.moon_angle) * (self.radius * 2.2)
        t.penup()
        t.goto(moon_x, moon_y)
        t.pendown()
        t.dot(4, "#D3D3D3")


class FallingStar:
    """Manages high-velocity shooting stars with dynamic tail scaling."""

    def __init__(self):
        self.reset()
        self.x = random.randint(-WIDTH // 2, WIDTH // 2)
        self.y = random.randint(-HEIGHT // 2, HEIGHT // 2)

    def reset(self):
        self.x = random.randint(-WIDTH // 2, WIDTH // 2 + 200)
        self.y = HEIGHT // 2 + random.randint(10, 150)
        self.speed = random.uniform(5, 11)
        self.length = random.randint(20, 45)
        self.color = random.choice(["#FFFFFF", "#E0FFFF", "#FFFFE0", "#FFD700"])
        self.size = random.randint(3, 5)

    def update(self):
        self.x -= self.speed
        self.y -= self.speed
        if self.x < -WIDTH // 2 - 50 or self.y < -HEIGHT // 2 - 50:
            self.reset()

    def draw(self, t):
        t.penup()
        t.goto(self.x, self.y)
        t.pendown()
        t.color(self.color)
        t.pensize(2)
        t.setheading(45)
        t.forward(self.length)

        t.pensize(1)
        t.penup()
        t.goto(self.x, self.y)
        t.pendown()
        t.dot(self.size, "#FFFFFF")


class UFO:
    """Simulates a hidden object crossing the canvas with blinking beacon nodes."""

    def __init__(self):
        self.reset()
        self.x = -WIDTH // 2 - 100

    def reset(self):
        self.x = -WIDTH // 2 - 200
        self.y = random.randint(-HEIGHT // 3, HEIGHT // 3)
        self.speed = random.uniform(3, 6)
        self.signal_timer = 0

    def update(self):
        self.x += self.speed
        self.signal_timer += 1
        if self.x > WIDTH // 2 + 100:
            self.reset()

    def draw(self, t):
        t.penup()
        t.goto(self.x, self.y)
        t.pendown()
        t.color("#708090")
        t.begin_fill()
        t.setheading(90)
        for _ in range(2):
            t.circle(30, 90)
            t.circle(10, 90)
        t.end_fill()

        t.penup()
        t.goto(self.x + 10, self.y + 8)
        t.pendown()
        t.color("#00FFFF")
        t.begin_fill()
        t.circle(10)
        t.end_fill()

        if self.signal_timer % 10 < 5:
            t.penup()
            t.goto(self.x - 15, self.y + 2)
            t.dot(4, "#FF0000")
            t.goto(self.x + 15, self.y + 2)
            t.dot(4, "#FF0000")
        else:
            t.penup()
            t.goto(self.x, self.y - 2)
            t.dot(4, "#00FF00")


class Spark:
    """Manages energy discharge particle fragments inside explosive cycles."""

    def __init__(self, x, y):
        self.x = x
        self.y = y
        angle = random.uniform(0, 2 * math.pi)
        speed = random.uniform(2, 7)
        self.dx = math.cos(angle) * speed
        self.dy = math.sin(angle) * speed
        self.life = random.randint(15, 30)
        self.color = random.choice(["#FF4500", "#FF8C00", "#FFD700", "#FFFFFF"])

    def update(self):
        self.x += self.dx
        self.y += self.dy
        self.life -= 1

    def draw(self, t):
        if self.life > 0:
            t.penup()
            t.goto(self.x, self.y)
            t.pendown()
            t.dot(max(2, self.life // 4), self.color)


# ==========================================
# INPUT LISTENER SYSTEM
# ==========================================
def trigger_supernova(x, y):
    for _ in range(40):
        explosions.append(Spark(x, y))


# ==========================================
# INITIALIZING SYSTEM POOLS
# ==========================================
drawer = turtle.Turtle()
drawer.hideturtle()
drawer.speed(0)

# Build centralized Solar System objects
central_sun = Sun(0, 0, 55)

# Planet parameters: center_x, center_y, orbit_radius, planet_radius, color, orbit_speed, name
earth = OrbitingPlanet(0, 0, 240, 14, "#1E90FF", 0.01, name="Earth")

# Adding Mercury as a fast inner planet to enhance visual complexity
mercury = OrbitingPlanet(0, 0, 110, 8, "#888888", 0.025, name="Mercury")

falling_stars = [FallingStar() for _ in range(30)]
ufo_ship = UFO()

# Link operating environment pointer events
screen.listen()
screen.onscreenclick(trigger_supernova)

# Heads-Up UI text printer configuration
ui_painter = turtle.Turtle()
ui_painter.hideturtle()
ui_painter.color("white")


# ==========================================
# CORE SIMULATION CONTROL ENGINE
# ==========================================
def run_simulation():
    drawer.clear()

    # 1. Render core stationary solar system anchor
    central_sun.draw(drawer)

    # 2. Update and draw systemic planet orbits
    mercury.update()
    mercury.draw(drawer)

    earth.update()
    earth.draw(drawer)

    # 3. Process UFO and meteor physics states
    ufo_ship.update()
    ufo_ship.draw(drawer)

    for star in falling_stars:
        star.update()
        star.draw(drawer)

    # 4. Filter and process explosions tracking array backwards
    for i in range(len(explosions) - 1, -1, -1):
        spark = explosions[i]
        spark.update()
        if spark.life <= 0:
            explosions.pop(i)
        else:
            spark.draw(drawer)

    # 5. Render HUD Overlay Interface elements
    ui_painter.clear()
    ui_painter.penup()
    ui_painter.goto(-WIDTH // 2 + 20, HEIGHT // 2 - 40)
    ui_painter.write("ORBIT ENGINE v2.0 || CLICK ANYWHERE TO SPAWN A SUPERNOVA",
                     font=("Courier", 12, "bold"))

    screen.update()
    screen.ontimer(run_simulation, 25)  # Triggers next cycle (~40 FPS refresh rate)


# ==========================================
# ENGINE BOOT SEQUENCE
# ==========================================
run_simulation()
screen.mainloop()
