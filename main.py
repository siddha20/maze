from learning.train import Train


if __name__ == "__main__":
	train = Train()

	train.make_game(traps=1, size=7, square_size=80, frame_limit=75, rendered=True, epochs=1000)
	train.run_game()



	



	

	


