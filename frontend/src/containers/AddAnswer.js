import React, { useState, useRef } from 'react'
import {
  Container,
  Grid,
  makeStyles,
  TextField,
  Button,
  Typography,
  Paper,
  Select,
} from '@material-ui/core';
import { connect } from 'react-redux'
import Editor from '../components/editor/tiny_editor/react_tiny/TinyEditorComponent';


const useStyles = makeStyles((theme) => ({
  root: {
    flexGrow: 1,
    direction: 'ltr',
  },
  background: {
    minHeight: `calc(100vh - 5em)`,
  },
  title: {
    fontSize: 40,
    paddingTop: theme.spacing(2),
    paddingBottom: theme.spacing(2),
  },
  paper: {
    padding: theme.spacing(2),
    margin: 'auto',
  },
}))

const Answer = () => {
  const classes = useStyles();
  const answerEl = useRef(null);
  const teachBoxEl = useRef(null);

  return (
    <div className={classes.root}>
      <Grid container justify='center' alignItems='center' className={classes.background}>
        <Grid
          xs={10}
          sm={8}
          item container
          justify='center'
          alignItems='stretch'
          direction='column'
          spacing={6}>
          <Grid item>
            <Typography gutterBottom variant='h3' className={classes.title} align='center'>
              افزودن پاسخ
            </Typography>
          </Grid>
          <Grid item >
            <Paper className={classes.paper}>
              <Grid
                container
                direction='column'
                justify='center'
                spacing={2}>
                <Grid item>
                  <Typography gutterBottom >
                    متن پاسخ:
                  </Typography>
                </Grid>
                <Grid item>
                  <Editor
                    ref={answerEl}
                    id="answerElement"
                    initContent='پاسخ مسئله را این‌جا بنویسید!' />
                </Grid>
                <Grid item>
                  <Typography gutterBottom >
                    جعبه‌ی تدریس:
                  </Typography>
                </Grid>
                <Grid item>
                  <TextField label='هدف مسئله' variant='outlined' gutterBottom fullWidth />
                </Grid>
                <Grid item>
                  <Editor
                    ref={teachBoxEl}
                    id="teachBoxElement"
                    initContent='نکات مرتبط با نحوه‌ی تدریس این مسئله را این‌جا بنویسید!' />
                </Grid>
                <Grid container item alignItems='center' justify='center' spacing={2}>
                  <Grid item>
                    <Select
                      variant='outlined'
                      native
                      // onChange={handleChange}
                      inputProps={{
                        name: 'age',
                        id: 'filled-age-native-simple',
                      }}
                    >
                      <option value={10}>سوال اول</option>
                      <option value={20}>سوال دوم</option>
                      <option value={30}>سوال سوم</option>
                    </Select>
                  </Grid>
                  <Grid item>
                    <Button variant='contained' color='primary'>
                      بزن بریم
                    </Button>
                  </Grid>
                </Grid>
              </Grid>
            </Paper>
          </Grid>
        </Grid>
      </Grid>
    </div>
  )
}

const mapStateToProps = (state, ownProps) => ({

})

export default connect(
  mapStateToProps,
  {

  }
)(Answer);