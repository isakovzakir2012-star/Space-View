This is a 2D interactive space simulation engine built using Python's turtle, random, and math modules. It renders a real-time mini solar system animation inside a graphical window with animated celestial objects and interactive effects.
Central Sun & Atmospheric Aura (Sun Class)
Draws a layered gradient sun at the origin (0, 0) using concentric circles that fade from yellow to orange/red to simulate solar heat/glow.
Orbital Mechanics (OrbitingPlanet Class)
Uses trigonometry (math.cos and math.sin) to calculate real-time continuous circular paths around the Sun.
Renders Mercury (fast inner orbit) and Earth (slower outer orbit with green continent details).
Calculates a local sub-orbit for Earth's Moon, allowing it to rotate around Earth as Earth orbits the Sun.
Background Celestial Effects
Shooting Stars (FallingStar Class): Generates 30 dynamic meteor lines falling diagonally across deep space with randomized colors, speeds, and resetting bounds.
Passing UFO (UFO Class): A saucer object that flies across the screen with a glass dome and blinking red/green signal lights.
Supernova Particle Explosions (Spark Class & Input Listener)
Tracks user mouse clicks using screen.onscreenclick().
Spawns 40 dynamic spark particles at the click location that burst outward in random angles and fade over time.
Engine Performance & HUD
Uses screen.tracer(0) and screen.ontimer() to create a custom double-buffered game loop running at ~40 FPS without window flickering.
Features an overlay Head-Up Display (HUD) showing controls and system title.
FallingStar	Ambient background meteor	Linear directional vectors with dynamic reset.
This is all info you need.
