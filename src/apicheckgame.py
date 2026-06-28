class ApiCheckGames:
    def validate_game_id(self, game_type, user_id, zone_id=""):
        # Contoh logika: Jika ID sesuai, kembalikan data sukses
        if user_id == "1084710366":
            return {
                "status": True,
                "message": "Success",
                "nickname": "Martinus Krisandro Perdana Putra"
            }
        return {"status": False, "message": "ID Tidak Ditemukan"}
