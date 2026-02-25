using System;
using System.Drawing;
using System.IO;
using System.Linq;
using System.Windows.Forms;

namespace PopupImageApp
{
    static class Program
    {
        [STAThread]
        static void Main()
        {
            Application.EnableVisualStyles();
            Application.SetCompatibleTextRenderingDefault(false);
            Application.Run(new MainForm());
        }
    }

    public class MainForm : Form
    {
        private Timer popupTimer;
        private string imageFolder = @"D:\Ophiuchus\offensive\oathkeeper\assets\images";
        private string popupFolder = @"D:\Ophiuchus\offensive\oathkeeper\assets\text";
        private Random rand = new Random();

        public MainForm()
        {
            FormBorderStyle = FormBorderStyle.None;
            WindowState = FormWindowState.Maximized;
            TopMost = true;
            BackColor = Color.Black;

            LoadRandomImage();
            StartPopupLoop();
        }

        private void LoadRandomImage()
        {
            if (!Directory.Exists(imageFolder)) return;

            var images = Directory.GetFiles(imageFolder, "*.png");
            if (images.Length == 0) return;

            string imagePath = images[rand.Next(images.Length)];

            PictureBox pictureBox = new PictureBox();
            pictureBox.Dock = DockStyle.Fill;
            pictureBox.SizeMode = PictureBoxSizeMode.Zoom;
            pictureBox.Image = Image.FromFile(imagePath);

            Controls.Add(pictureBox);
        }

        private void StartPopupLoop()
        {
            popupTimer = new Timer();
            popupTimer.Interval = 3000; // time between popups
            popupTimer.Tick += (s, e) => SpawnPopup();
            popupTimer.Start();
        }

        private void SpawnPopup()
        {
            if (!Directory.Exists(popupFolder)) return;

            var files = Directory.GetFiles(popupFolder, "*.txt");
            if (files.Length == 0) return;

            string text = File.ReadAllText(files[rand.Next(files.Length)]);
            PopupForm popup = new PopupForm(text);
            popup.Show();
        }
    }

    public class PopupForm : Form
    {
        private Timer animationTimer;
        private int speed = 8;

        public PopupForm(string message)
        {
            Size = new Size(300, 150);
            FormBorderStyle = FormBorderStyle.FixedToolWindow;
            TopMost = true;
            StartPosition = FormStartPosition.Manual;

            int screenWidth = Screen.PrimaryScreen.Bounds.Width;
            int screenHeight = Screen.PrimaryScreen.Bounds.Height;

            Random rand = new Random();
            int startX = rand.Next(0, screenWidth - Width);
            Location = new Point(startX, screenHeight);

            Label label = new Label();
            label.Text = message;
            label.Dock = DockStyle.Fill;
            label.TextAlign = ContentAlignment.MiddleCenter;
            label.Font = new Font("Arial", 12);
            Controls.Add(label);

            animationTimer = new Timer();
            animationTimer.Interval = 20;
            animationTimer.Tick += AnimateUp;
            animationTimer.Start();
        }

        private void AnimateUp(object sender, EventArgs e)
        {
            Top -= speed;

            if (Bottom < 0)
            {
                animationTimer.Stop();
                Close();
            }
        }
    }
}