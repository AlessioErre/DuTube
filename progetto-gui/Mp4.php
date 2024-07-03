4
<?php
class Mp4{
  // Proprietà private
  private $mp4 = "22";
  private $link;

  // Costruttore
  public function __construct($mp4, $link) {
    $this->mp4 = $mp4;
    $this->link = $link;
  }

  // Metodo pubblico per accedere alla proprietà nome
  public function getMp4() {
    return $this->mp4;
  }

  // Metodo pubblico per accedere alla proprietà cognome
  public function getLink() {
    return $this->link;
  }


   public function Mp4Audio(){
      system("python3 /home/black-jack/05-Script/03-Altrui/yt-dlp/yt_dlp/__main__.py -f " . $this->mp4 . " -P /home/black-jack/05-Script/DuTube/Downloads " . $this->link);
   }}

$mp4 = "22";
$audio = new Mp4($mp4, $argv[1]);
$audio->Mp4Audio();

