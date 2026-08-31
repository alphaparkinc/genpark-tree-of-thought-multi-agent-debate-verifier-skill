from client import TreeOfThoughtMultiAgentDebateVerifierClient

def main():
    client = TreeOfThoughtMultiAgentDebateVerifierClient()
    res = client.conduct_debate_verification('Is P vs NP resolvable within ZFC set theory?')
    print('Tree-of-Thought Debate Verifier: ' + res['debate_session_id'])
    print('Tree Depth: ' + str(res['tree_depth_explored']) + ' | Refuted Arguments: ' + str(res['arguments_refuted_count']))
    print('Consensus: ' + str(res['epistemic_consensus_score_pct']) + '% | Verdict: ' + res['verdict'])
    print('Transcript: ' + res['debate_graph_transcript_url'])

if __name__ == '__main__':
    main()
