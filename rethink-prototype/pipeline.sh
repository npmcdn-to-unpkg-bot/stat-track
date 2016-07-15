# jq script rewritten to work with
# the rethink prototype

python prep_for_jq.py | \
jq '[.[] | {
    name: .user.name,
    time: .created_at,
    timezone: .user.time_zone,
    text: .text,
    hashtags: .entities.hashtags,
    retweets: .retweet_count,
    location: .user.location,
    lang: .user.lang,
    mentions: .entities.user_mentions,
    retweet_text: .retweeted_status.text,
    retweet_favorite: .retweeted_status.favorite_count
    }]' | \
python done_with_jq.py
