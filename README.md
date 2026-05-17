# DropDash 🎮

A fun, fast-paced Pygame adventure where you catch falling apples and rack up points! Dodge obstacles and test your reflexes in this classic arcade-style game.

## 📋 Overview

DropDash is a casual arcade game built with Pygame. Navigate your character left and right to catch falling apples before they hit the ground. Collect as many apples as possible to increase your score!

## 🎮 How to Play

### **Controls**
- **LEFT ARROW** - Move player left
- **RIGHT ARROW** - Move player right
- **SPACE** - Restart game after Game Over

### **Objective**
- Catch falling apples with your character
- Each apple caught = **+1 point**
- If an apple reaches the ground, **GAME OVER**
- Try to get the highest score possible!

### **Gameplay Tips**
- Move smoothly to intercept apples before they fall
- Apples spawn randomly across the top of the screen
- Your character animates while moving - watch the walking sprites!
- Listen for audio feedback: collect sound when catching apples, lose sound on Game Over

## 🚀 Getting Started

### **Requirements**
- Python 3.7 or higher
- Pygame library

### **Installation**

1. **Clone or download the project:**
   ```bash
   git clone https://github.com/Nurusov2011/DropDash-On-Pygame.git
   cd DropDash
   ```

2. **Install dependencies:**
   ```bash
   pip install pygame
   ```

### **Running the Game**

**Option 1: Run Python script**
```bash
python DropDash.py
```

**Option 2: Run compiled executable** (Windows)
```bash
DropDash.exe
```

## 📁 Project Structure

```
DropDash/
├── DropDash.py           # Main game code
├── DropDash.exe          # Compiled executable
├── README.md             # This file
├── icon.png              # Window icon
├── sky2.png              # Background sky
├── grass.png             # Ground sprite
├── player.png            # Player sprite (right-facing)
├── player2.png           # Player sprite (left-facing)
├── apple.png             # Falling apple sprite
├── collect.wav           # Sound effect (apple caught)
└── lose.mp3              # Sound effect (game over)
```

## 🎨 Features

✨ **Smooth Animation** - Character walking animation while moving  
🔊 **Audio Feedback** - Collect and game-over sound effects  
🎯 **Simple Controls** - Intuitive left/right arrow movement  
📊 **Score Tracking** - Real-time score display  
🎮 **Game States** - Active gameplay and game-over screen  
🎨 **Pixel Art** - Clean, retro-style graphics  

## 🔧 Technical Details

- **Built with:** Python 3 + Pygame
- **Resolution:** 400x800 pixels
- **FPS:** 60 frames per second
- **Game Loop:** Event-driven with smooth physics

## 📈 Future Enhancements

- [ ] Difficulty progression (increasing drop speed)
- [ ] High score persistence (save to file)
- [ ] Power-ups and special items
- [ ] Obstacles to avoid
- [ ] Multiple levels
- [ ] Leaderboard system
- [ ] Pause functionality
- [ ] Main menu screen
- [ ] Sound volume control
- [ ] Mobile/touch support

## 🐛 Known Issues / Limitations

- No pause button during gameplay
- No persistent high score tracking
- Fixed difficulty (no progression)
- Limited to keyboard input only

## 💡 Tips for Developers

If you want to modify or enhance the game:
- Adjust apple speed: Change `apple_rect.bottom += 11` to a different value
- Change player speed: Modify the `5` in player movement code
- Adjust screen size: Change `pygame.display.set_mode((400,800))`
- Add more sprites: Load additional player or apple images

## 📝 License

Free to use and modify. Credit appreciated!

## 👤 Author

**Nurusov2011** - Your First Pygame Project! 🎓

---

**Enjoy the game and happy coding! 🚀**
