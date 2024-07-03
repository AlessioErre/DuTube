
<?php
class Mp3{
  // Proprietà private
  private $mp3 = "mp3";
  private $link;

  // Costruttore
  public function __construct($mp3, $link) {
    $this->mp3 = $mp3;
    $this->link = $link;
  }

  // Metodo pubblico per accedere alla proprietà nome
  public function getMp3() {
    return $this->mp3;
  }

  // Metodo pubblico per accedere alla proprietà cognome
  public function getLink() {
    return $this->link;
  }


   public function Mp3Audio(){
      system("/home/black-jack/.pyenv/versions/3.11.2/bin/python3.11 /home/black-jack/05-Script/03-Altrui/yt-dlp/yt_dlp/__main__.py -x --audio-format " . $this->mp3 . " -P /home/black-jack/05-Script/DuTube/Downloads " . $this->link);
   }}

$mp3 = "mp3";
$audio = new Mp3($mp3, $argv[1]);
$audio->Mp3Audio();

