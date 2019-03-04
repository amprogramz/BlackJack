##################################################################
#                    Dealer class
#
# Contains dealer class
# Contains the logic for how the dealer plays
#
# author: Bobby
##################################################################

class Dealer:
	def __init__(self):
		x = 1

	def get_bets(player_list):
		for player in player_list:
			if player.state == PlayerState.PLAYING:
				player_bet = player.get_bet()
				if player_bet == 0:
					player.state = PlayerState.DONE
				elif player.chips - player_bet < 0:
					player_bet = player.chips

	def deal(player_list, dealer, deck):
		for i in range(NUM_DEAL_CARDS):
			for player in player_list:
				if player.state == PlayerState.PLAYING:
					deck.draw(player)
			deck.draw(dealer)
		dealer.flip_card(CardState.DOWN)

	def check_blackjack(player_list, dealer):
		for player in player_list:
			if calc_cards(player) == BLACKJACK:
				player.state = PlayerState.HAS_BLACKJACK
		if calc_cards(dealer) == BLACKJACK:
			dealer.state = PlayerState.HAS_BLACKJACK
		if dealer.state == PlayerState.HAS_BLACKJACK:
			for player in player_list:
				if PlayerState != PlayerState.HAS_BLACKJACK:
					player.state = PlayerState.LOSS

	def player_actions(player_list, dealer):
		if dealer.state != PlayerState.HAS_BLACKJACK:
			all_bust = true
			for player in player_list:
				while (player.state == PlayerState.PLAYING):
					player_move = player.get_play()
					if player_move == PlayerMove.HIT:
						deck.get_card(player)
					elif player_move == PlayerMove.STAND:
						player.state = PlayerState.DONE
						all_bust = false
					if calc_cards(player) >= BUST
						player.state = PlayerState.LOSS
			if all_bust != true:
				dealer.flip_card(CardState.UP)
				while (dealer.state == PlayerState.PLAYING):
					dealer_move = dealer.get_play()
					if dealer_move == PlayerMove.HIT:
						deck.get_card(dealer)
					elif dealer_move == PlayerMove.STAND:
						dealer.state = PlayerState.DONE
					if calc_cards(dealer) >= BUST
						dealer.state = PlayerState.LOSS

	def check_player_states(player_list, dealer)
		is_finished = true
		for player in player_list:
			if player.chips == 0:
				player.state = PlayerState.DONE
			else:
				player.state = player.get_state()
			if player.state == PlayerState.PLAYING:
				is_finished = false
			if is_finished == true:
				dealer.state = PlayerState.DONE

	def calc_payouts(player_list, dealer):
		dealer_hand = calc_cards(dealer)

def dealer_logic():
	deck = Deck(NUM_OF_DECKS)
	while (dealer.state == PlayerState.PLAYING):
		get_bets(player_list)
		deal(player_list, dealer, deck)
		check_blackjack(player_list, dealer)
		player_actions(player_list, dealer, deck)
		calc_payouts(player_list, dealer)
		check_deck()
		check_player_states(player_list, dealer)
