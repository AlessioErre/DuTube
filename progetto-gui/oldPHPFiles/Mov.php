
<?php
class Mov{
  // Proprietà private
  private $mov = "mov";
  private $link;

  // Costruttore
  public function __construct($mov, $link) {
    $this->mov = $mov;
    $this->link = $link;
  }

  // Metodo pubblico per accedere alla proprietà nome
  public function getMov() {
    return $this->mov;
  }

  // Metodo pubblico per accedere alla proprietà cognome
  public function getLink() {
    return $this->link;
  }


   public function MovAudio(){
      system("/home/black-jack/.pyenv/versions/3.11.2/bin/python3.11 /home/black-jack/05-Script/03-Altrui/yt-dlp/yt_dlp/__main__.py --recode-video " . $this->mov . " -P /home/black-jack/05-Script/DuTube/Downloads " . $this->link);
   }}

$mov = "mov";
$audio = new Mov($mov, $argv[1]);
$audio->MovAudio();

