
<?php
class Ogg{
  // Proprietà private
  private $ogg = "vorbis";
  private $link;

  // Costruttore
  public function __construct($ogg, $link) {
    $this->ogg = $ogg;
    $this->link = $link;
  }

  // Metodo pubblico per accedere alla proprietà nome
  public function getOgg() {
    return $this->ogg;
  }

  // Metodo pubblico per accedere alla proprietà cognome
  public function getLink() {
    return $this->link;
  }


   public function OggAudio(){
      system("/home/black-jack/.pyenv/versions/3.11.2/bin/python3.11 /home/black-jack/05-Script/03-Altrui/yt-dlp/yt_dlp/__main__.py -x --audio-format " . $this->ogg . " -P /home/black-jack/05-Script/DuTube/Downloads " . $this->link);
   }}

$ogg = "vorbis";
$audio = new Ogg($ogg, $argv[1]);
$audio->OggAudio();

