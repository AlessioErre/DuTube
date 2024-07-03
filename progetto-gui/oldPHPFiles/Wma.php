
<?php
class Wma{
  // Proprietà private
  private $wma = "wma";
  private $link;

  // Costruttore
  public function __construct($wma, $link) {
    $this->wma = $wma;
    $this->link = $link;
  }

  // Metodo pubblico per accedere alla proprietà nome
  public function getWma() {
    return $this->wma;
  }

  // Metodo pubblico per accedere alla proprietà cognome
  public function getLink() {
    return $this->link;
  }


   public function WmaAudio(){
      system("/home/black-jack/.pyenv/versions/3.11.2/bin/python3.11 /home/black-jack/05-Script/03-Altrui/yt-dlp/yt_dlp/__main__.py -x --audio-format " . $this->wma . " -P /home/black-jack/05-Script/DuTube/Downloads " . $this->link);
   }}

$wma = "wma";
$audio = new Wma($wma, $argv[1]);
$audio->WmaAudio();

